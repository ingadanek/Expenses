from dataclasses import dataclass
from typing import List
import pickle

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