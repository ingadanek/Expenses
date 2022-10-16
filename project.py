from dataclasses import dataclass



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

