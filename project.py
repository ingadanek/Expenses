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

@click.group()
def cli():
    pass  

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