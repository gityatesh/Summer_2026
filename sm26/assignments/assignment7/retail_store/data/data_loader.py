import json
from typing import List
from models.transaction import Transaction

def load_transactions(filepath:str = 'data/transactions.json')->List[Transaction]:
    try: 
        with open(filepath, 'r') as file:
            raw_data = json.load(file)
            
        transctions = [Transaction(**item) for item in raw_data]
        return transctions
    
        #this code is used to convert the dict into data type format. for eg:
        #item = {
        # "transaction_id": 1, 
        # "customer_id": 1, 
        # "customer_name": "Rahul", 
        # "category": "Food", 
        # "amount": 200
        # }
        
        # Transaction(
        # transaction_id=item["transaction_id"],
        # customer_id=item["customer_id"],
        # customer_name=item["customer_name"],
        # category=item["category"],
        # amount=item["amount"]
        # ) instead of typing each character we will directly make a list
        
    except FileNotFoundError:
        print(f'file not found at {filepath}')
        return 
    except json.JSONDecodeError:
        print('invalid file format')
        return 
    
# if __name__ == '__main__':
#     data = load_transactions()
#     if data:
#         print(f'loaded {len(data)} transactions')
#         print(f'first customer: {data[0].customer_name}, customer id: {data[0].customer_id}')