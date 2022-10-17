# Tracking Expenses

Using Python and its packages to write a program that helps to track expenses. One can easily add new expenses and generate reports.

## How to use
The program has the following subcommands: add, report, export-python and import-csv.

Using one's preferred code editor (e.g. VSCode), user enters keyword 'python' and filepath followed by one of the subcommands listed above. 

The add subcommand allows a new expense to be added. The amount (as int) and description (in inverted commas) must then be given as further command line arguments.
For example: `python Expenses/project.py add 100 "money for shopping"`

The report subcommand displays all the expenses in the table. There is also a "big?" column in the table, where there is a tick when the expense is big, i.e. at least 1,000. In addition, the total of all expenses is displayed at the very end. 
For example: `python Expenses/project.py report`

The export-python subcommand displays a list of all expenses as an object.
For example: `python Expenses/project.py export-python`

The import-csv subcommand imports a list of expenses from a CSV file.
For example: `python Expenses/project.py import-csv Expenses/expenses.csv`


## Code and Resources Used
**Python Version:** `3.10.6`

**Packages:** `click, csv, dataclass, typing, pickle, sys` 

