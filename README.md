

# Cledara Tripletex Converter
=====================================

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This is a tool to convert Cledara transactions into a format compatible with Tripletex, a Norwegian accounting system. The converter takes a Cledara transactions CSV file export of transactions as input and generates a file that can be imported into Tripletex (Mamut GBAT10 format).


## Custom Fields in Cledara
The following custom fields must be defined and used in Cledara:

* Tripletex Expense Account
* Tripletex VAT Code
* Tripletex Supplier Number


## VAT Settings
Cledara payments are associated with one of six different VAT codes:

* 1
* 13
* 86-89

The default/fallback VAT code is 86.

## Requirements
* Python 3.8 or higher
* Poetry (https://python-poetry.org/)


## Installation
Clone the repository and run `poetry install` to install dependencies

## Using the tool
To use the converter, simply run `poetry run cledara-tripletex path/to/transactions.csv`. The converter will generate a file (cledara_transactions_for_tripletex.csv) that can be imported into Tripletex.

## Configuration Options

The converter accepts the following configuration options:

* `--card-asset-account`: The account number for the card asset account.
* `--voucher-type`: The voucher type to use for the transactions.

These options can be specified as command-line arguments.


## Import the file to Tripletex
To import the generated file to Tripletex, follow these steps:

1. Navigate to “Voucher” > “Import” in Tripletex.
2. Select “Mamut GBAT10” as the File type.
3. Select “UTF-8” as the Encoding.
4. Select “Let Tripletex generate VAT entries”, but deselect “External Vat code “1”.
5. Upload the file converted with this tool.
6. Press “Import” on the bottom left of the screen.



<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

Stig Christian Aske - stigchristian@me.com
