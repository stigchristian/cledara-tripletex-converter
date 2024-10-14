from typing import Literal, Optional

from pydantic import BaseModel


# GBAT10 Reference docs
# Tripletext docs:
# https://hjelp.tripletex.no/hc/no/articles/4411155692945-How-to-import-vouchers-with-Mamut-GBAT10-format
# Original format docs from Mamut:
# https://help.mamut.com/no/mhelp/rtm/import_export/csv_formats/journal_formats/gbat10.htm
class AccountingEntry(BaseModel):
    identification: str = "GBAT10"  # 1 Always equal to "GBAT10"
    voucher_number: Optional[int] = None  # 2 used to differentiate vouchers
    voucher_date: str  # 3 Date in the format YYYYMMDD
    voucher_type: Optional[int] = (
        None  # 4 A number series is created for each voucher type.
    )
    period: Optional[int] = None  # 5 IGNORED BY TRIPLETEX
    fiscal_year: Optional[int] = None  # 6 IGNORED BY TRIPLETEX
    account: int  # 7
    vat_code: Optional[int] = None  # 8 ,
    net_amount: Optional[float] = (
        None  # 9 Two decimals. IGNORED BY TRIPLETEX IF «Generate VAT postings» IS CHECKED
    )
    customer_number: Optional[int] = None  # 10
    supplier_number: Optional[int] = None  # 11
    contact_name: str  # 12
    address: Optional[str] = None  # 13
    postal_code: Optional[str] = None  # 14
    city: Optional[str] = None  # 15
    invoice_number: Optional[str] = None  # 16 IGNORED BY TRIPLETEX
    kid: Optional[str] = None  # 17 IGNORED BY TRIPLETEX
    due_date: Optional[str] = None  # 18 IGNORED BY TRIPLETEX
    unused_field: Optional[str] = None  # 19 IGNORED BY TRIPLETEX
    bank_account: Optional[str] = None  # 20 IGNORED BY TRIPLETEX
    ledger_description: Optional[str] = None  # 21
    subledger_description: Optional[str] = None  # 22 IGNORED BY TRIPLETEX
    interest_invoicing: Optional[Literal[1, 2, 3]] = None  # 23 IGNORED BY TRIPLETEX
    project: Optional[int] = None  # 24
    department: Optional[int] = None  # 25
    payment_terms: Optional[int] = None  # 26
    generate_vat_postings: Optional[Literal["T", "F"]] = (
        None  # 27 True (T) if Tripletex should generate VAT postings., or False (F) if this row should be ignored.
    )
    gross_amount: float  # 28 two decimals
    iban: Optional[str] = None  # 29 IGNORED BY TRIPLETEX
    swift_bic: Optional[str] = None  # 30 IGNORED BY TRIPLETEX
