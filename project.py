from dataclasses import dataclass
from typing import List
import pickle
import sys 

import click

BIG_EXPENSE_THRESHOLD = 1000
DB_FILENAME = 'budget.db'

@dataclass
class Expense:
    id: int
    amount: float
    description: str
        
    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount cannot be zero or negative")

    def is_big(self) -> bool:
        return self.amount >= BIG_EXPENSE_THRESHOLD

def load_or_init() -> List[Expense]:
    try:  
        with open(DB_FILENAME, 'rb') as stream:
            expenses = pickle.load(stream)
    except FileNotFoundError:
        expenses = []
    return expenses

def save_expenses(expenses: List[Expense]) -> None: 
    with open(DB_FILENAME, 'wb') as stream:
        pickle.dump(expenses, stream)

def find_next_id(expenses: List[Expense]) -> int:
    all_ids = {expense.id for expense in expenses}
    next_id = 1
    while next_id in all_ids:
        next_id += 1
    return next_id

def compute_total(expenses):
    total_list = [expense.amount for expense in expenses]
    total = sum(total_list)
    return total

def print_report(expenses: List[Expense], total: int) -> None:
    if expenses:
        print(f'--ID--  -AMOUNT-  -BIG?-  --DESC------')
        for expense in expenses:
            if expense.is_big():
                big = '(!)'
            else:
                big = ''
            print(f'{expense.id:6} {expense.amount:8} {big:^10} {expense.description}')
        
        print(f'TOTAL: {total:8}')
    else:
        print('You did not provide any expenses yet')

@click.group()
def cli():
    pass  

@cli.command()
def report() -> None:
    expenses = load_or_init()
    total = compute_total(expenses)
    print_report(expenses, total)


@cli.command()
@click.argument('amount', type=int) 
@click.argument('description') 
def add(amount: int, description: str) -> None:
    expenses = load_or_init()

    try:
        new_expense = Expense(
            id=find_next_id(expenses),
            amount=amount,
            description=description
        )
    except ValueError as e:
        print(f'error: {e.args[0]}')
        sys.exit(1)

    expenses.append(new_expense)
    save_expenses(expenses)
    print('added:)')