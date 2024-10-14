import typer
from pathlib import Path
import csv
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class AccountingEntry:
    identification: str = "GBAT10"  # Always equal to "GBAT10"
    voucher_number: Optional[int]  # Numeric, used to differentiate vouchers
    voucher_date: str  # Date in the format YYYYMMDD
    voucher_type: int  # Numeric, related to StdReg_xxx.xls
    period: int  # Numeric, no decimals
    fiscal_year: int  # Numeric, no decimals
    account: int  # Numeric, no decimals
    vat_code: int  # Numeric, related to StdReg_xxx.xls
    balance: float  # Numeric, with two decimals
    customer_number: Optional[int]  # Numeric, required for receivables
    supplier_number: Optional[int]  # Numeric, required for payables
    contact_name: Optional[str]  # Text, required if contact is new or to overwrite existing name
    address: Optional[str]  # Text
    postal_code: Optional[str]  # Text
    city: Optional[str]  # Text
    invoice_number: Optional[str]  # Text
    kid: Optional[str]  # Text
    due_date: Optional[str]  # Date in format YYYYMMDD
    unused_field: Optional[str]  # This field must be included but can be left blank
    bank_account: Optional[str]  # Text
    general_ledger_description: Optional[str]  # Text
    subledger_description: Optional[str]  # Text
    interest_invoicing: Optional[int]  # 1 = No interest, 2 = Always, 3 = Only after 30 days
    project: Optional[int]  # Numeric or blank for none
    department: Optional[int]  # Numeric, related to StdReg_xxx.xls
    payment_terms: Optional[int]  # Numeric, related to StdReg_xxx.xls
    gross: Optional[bool]  # Blankt, True (T), or False (F)
    gross_sum: Optional[float]  # Numeric, with two decimals
    iban: Optional[str]  # Alphanumeric
    swift_bic: Optional[str]  # Alphanumeric




def main(transactions_file: Path):
    print(f"Converting {transactions_file}")

    with transactions_file.open("r") as fp:
        transactions = csv.DictReader(fp)

        output = []

        for transaction in transactions:
            print(transaction)

            AccountingEntry(
                voucher_date=datetime.strptime(transaction["Transaction date"], "%d/%m/%Y").strftime("%Y%m%d"),
                voucher_type=100,
                

            )








if __name__ == "__main__":
    typer.run(main)

