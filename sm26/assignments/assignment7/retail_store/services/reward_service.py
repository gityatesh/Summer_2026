from typing import Tuple, List, Dict


class RewardService:
    
    def calculate_reward(self, ranked_customers: List[Tuple[Tuple[int, str], int]])->List[Dict]:
        reward_details = []
        if len(ranked_customers)>0:
            cust_id,name = ranked_customers[0][0]
            total_spent = ranked_customers[0][1]
            reward_details.append({'ID': cust_id, 'Name': name, 'Discount': total_spent * 0.10})
            
        if len(ranked_customers)>1:
            cust_id,name = ranked_customers[1][0]
            total_spent = ranked_customers[1][1]
            reward_details.append({'ID': cust_id, 'Name': name, 'Discount': total_spent * 0.05})
        return reward_details  
    
    def calculate_cupouns(self, ranked_customers: List[Tuple[Tuple[int, str], int]]) -> List[dict]:
        cupoun_details = []
        if len(ranked_customers)>0:
            cust_id,name = ranked_customers[-1][0]
            total_spent = ranked_customers[-1][1]
            cupoun_details.append({'ID': cust_id, 'Name': name, 'Cupoun Value': total_spent * 0.1})
            
        if len(ranked_customers)>1:
            cust_id,name = ranked_customers[-2][0]
            total_spent = ranked_customers[-2][1]
            cupoun_details.append({'ID': cust_id, 'Name': name, 'Cupoun Value': total_spent * 0.05})
        return cupoun_details    