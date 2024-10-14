import csv
from datetime import datetime
from pathlib import Path
from typing import Optional

import typer

from cledara_tripletex.models.accounting_entry import AccountingEntry

DEFAULT_CARD_ASSET_ACCOUNT = 1920
DEFAULT_EXPENSE_ACCOUNT = 6810
DEFAULT_VAT_CODE = 86

cli = typer.Typer()


@cli.command()
def main(
    cledara_transactions_file: Path,
    card_asset_account: int = DEFAULT_CARD_ASSET_ACCOUNT,
    voucher_type: Optional[int] = None,
):
    print(f"Converting {cledara_transactions_file}")

    output: list[AccountingEntry] = []

    with cledara_transactions_file.open("r") as fp:
        transactions = csv.DictReader(fp)

        for transaction in transactions:
            if transaction["Money move"] != "debit":
                continue

            if transaction["Transaction date"].startswith("Exported on "):
                continue

            voucher_date = datetime.strptime(
                transaction["Transaction date"], "%d/%m/%Y"
            ).strftime("%Y%m%d")
            debit_amount = float(transaction["Transaction amount"])
            credit_amount = -debit_amount
            supplier_number = transaction["Tripletex Supplier Number"] or None
            contact_name = transaction["Reference"]
            ledger_description = f"Cledara [{transaction["Cledara ID"]}]: {transaction["Reference"]} | [{transaction["Local currency"]} {-float(transaction["Local amount"].replace(",",""))} @ {transaction["FX rate"]}] | ({credit_amount} EUR)"

            # Credit
            credit = AccountingEntry(
                voucher_date=voucher_date,
                voucher_type=voucher_type,
                account=transaction["Tripletex Expense Account"]
                or DEFAULT_EXPENSE_ACCOUNT,
                vat_code=transaction["Tripletex VAT Code"] or DEFAULT_VAT_CODE,
                net_amount=credit_amount,
                supplier_number=supplier_number,
                contact_name=contact_name,
                gross_amount=credit_amount,
                ledger_description=ledger_description,
                generate_vat_postings="T",
            )

            output.append(credit)

            # Debit
            debit = AccountingEntry(
                voucher_date=voucher_date,
                voucher_type=voucher_type,
                account=card_asset_account,
                net_amount=debit_amount,
                supplier_number=supplier_number,
                contact_name=contact_name,
                gross_amount=debit_amount,
                ledger_description=ledger_description,
                generate_vat_postings="T",
            )

            output.append(debit)

    with Path("cledara_transactions_for_tripletex.csv").open("w") as fp:
        writer = csv.DictWriter(
            fp, fieldnames=AccountingEntry.model_fields.keys(), delimiter=";"
        )
        writer.writerows([o.model_dump(exclude_none=True) for o in output])


if __name__ == "__main__":
    cli()
