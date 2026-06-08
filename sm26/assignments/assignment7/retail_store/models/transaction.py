from dataclasses import dataclass

@dataclass
class Transaction:
    transaction_id:int
    customer_id:int
    customer_name:str
    category:str
    amount:int