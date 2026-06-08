from typing import Dict, List, Tuple
from models.transaction import Transaction

class CustomerService:
    def __init__(self, transaction: List[Transaction]):
        self.transaction = transaction
        
    def get_customer_spending(self) -> Dict[Tuple[int, str], int]:
        spending={}
        for t in self.transaction:
            customer_details = (t.customer_id, t.customer_name)
            spending[customer_details] = spending.get(customer_details,0)+t.amount 
        return spending
    
    def get_customer_ranking(self) -> List[Tuple[str, int]]:
        spending = self.get_customer_spending()
        ranked = sorted(spending.items(), key = lambda x: x[1], reverse = True)
        return ranked
    
    def get_category_sales(self) -> Dict[str, int]:
        categorywise_spending = {}
        for t in self.transaction:
            categorywise_spending[t.category] = categorywise_spending.get(t.category, 0) + t.amount
        return categorywise_spending
    
    def search_customer_transactions(self, cust_id:int)->List[Transaction]:
        req_details =[]
        for t in self.transaction:
            if t.customer_id == cust_id:
                req_details.append(t)
        return req_details
    
    def find_duplicate_customers(self) -> set:
        seen = set()
        duplicate = set()
        for t in self.transaction:
            if t.customer_id in seen:
                duplicate.add(t.customer_id)
            else:
                seen.add(t.customer_id)
                
        return duplicate
    