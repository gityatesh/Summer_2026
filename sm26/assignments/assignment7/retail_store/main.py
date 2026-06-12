from data.data_loader import load_transactions
from services.customer_service import CustomerService
from services.reward_service import RewardService
from services.report_service import ReportServices

def run_application():
    # 1. Boot up the Data Layer
    print("Initializing Retail Store System...")
    transactions = load_transactions()
    
    if not transactions:
        print("Fatal Error: Could not load data. Shutting down.")
        return

    # 2. Boot up the Services
    # We hand the raw data to the Customer Service so it can do the math
    customer_service = CustomerService(transactions)
    
    # Reward and Report services don't need the raw data on boot
    reward_service = RewardService()
    report_service = ReportServices()

    # 3. Test the connection 
    while True:
            
            print("\n_______RETAIL STORE MENU________")
            print("1. View Customer Spending Report")
            print("2. View Category Sales Report")
            print("3. Search Customer Transactions")
            print("4. View Cashback Rewards")
            print("5. View Coupon Details")
            print("6. Generate Reports")
            print("7. Exit")
            
            choice = int(input('Enter your input: '))
            if choice == 1:
                spending = customer_service.get_customer_spending()
                print("Customer Spending Data:")
                for cust_tuple, amount in spending.items():
                    print(f"ID: {cust_tuple[0]} | Name: {cust_tuple[1]} -> ${amount}")

            elif choice == 2:
                categorywise = customer_service.get_category_sales()
                for category, categoryamount in categorywise.items():
                    print(f'Category: {category} -> ${categoryamount}')

            elif choice == 3:
                cust_id = int(input("Enter Customer ID: "))
                cust_transactions = customer_service.search_customer_transactions(cust_id)
                if cust_transactions:
                    print(f'Transactions for customer ID: {cust_id}')
                    for t in cust_transactions:
                        print(f'Transaction ID: {t.transaction_id}| Name: {t.customer_name}| Category: {t.category}| Amount Spent: {t.amount}')

            elif choice == 4:
                rankedcustomers = customer_service.get_customer_ranking()
                cashbackdetails = reward_service.calculate_reward(rankedcustomers)
                print(cashbackdetails)

            elif choice == 5:
                rankedcustomers = customer_service.get_customer_ranking()
                cupoundetails = reward_service.calculate_cupouns(rankedcustomers)
                print(cupoundetails)

            elif choice == 6:
                print('Generating Reports....')
                report_service.save_report('Individual Expense', {f'{k[1]}': v for k, v in customer_service.get_customer_spending().items()})
                report_service.save_report('Categorywise Report', customer_service.get_category_sales())
                
                total_cust = len(customer_service.get_customer_spending())
                total_transactions = len(transactions)
                total_revenue = sum(t.amount for t in transactions)
                ranked = customer_service.get_customer_ranking()
                higest_spender = ranked[0][0][0] if ranked else 'N.A.'
                lowest_spender = ranked[-1][0][0] if ranked else 'N.A.'
                category_dict = customer_service.get_category_sales()
                popular_category = max(category_dict, key = category_dict.get)
                
                report_service.generate_summary(total_cust, total_transactions, total_revenue, 
                                                higest_spender, lowest_spender, popular_category)
                
            elif choice == 7:
                print("Thank you for using Retail Store System!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_application()