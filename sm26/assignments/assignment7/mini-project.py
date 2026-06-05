import json

transactionslist = [
(1,1,"Rahul", "Food", 200),
(2,2,"Aman", "Travel", 500),
(3,1,"Rahul", "Food", 150),
(4,3,"Neha", "Shopping", 1200),
(5,2,"Aman", "Travel", 300),
(6,4,"Karan", "Food", 400),
(7,3,"Neha", "Shopping", 800),
(8,1,"Rahul", "Travel", 250)
]

class retailstoreas:
    def __init__(self):
        try: 
            with open('T.txt' ,'r') as file:
                self.transactions = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.transactions = []
        
    def showdata(self):
        with open('T.txt' ,'r') as file:
            lines = file.readlines()
        for line in lines:
            print(line)
        return
         
    def savedata(self):
        with open('T.txt', 'w') as file:
            json.dump(self.transactions, file)
            
    def insertinitialdata(self, transactionlist):
        self.transactions = transactionlist
        self.savedata()
        print('Data inserted successfully!')
        
    def appenddata(self, trans_id:int, cust_id:int, name:str, category:str, amount:int):
        for transaction in self.transactions:
            if transaction[0]==trans_id:
                print('This customer transaction already exists!')
                return
            
        self.transactions.append((trans_id, cust_id, name, category, amount))
        self.savedata()
        self.showdata()
        
    def removetransaction(self, trans_id):
        for transaction in self.transactions:
            if  transaction[0] == trans_id:
                self.transactions.remove(transaction)
                self.savedata()
                print('transaction removed successfully!')
                return 
        print('transaction not found!')
        
    def removecustomer(self, cust_id):
        self.transactions = [
        transaction
        for transaction in self.transactions
        if transaction[1] != cust_id
    ]

        self.savedata()
    print('customer removed successfully!')
        
# -----------------------------------------------------------------------------------------------------------       
    #question1: spending summary   
    def spendingsummary(self):
        
        customerspendingreport = []
        
        totalmoneyspent = {}
        for transaction in self.transactions:
            cust_details = (transaction[1],transaction[2])
            totalmoneyspent[cust_details] = totalmoneyspent.get(cust_details, 0)+transaction[4]
        print('Total expenditure per customer: ')    
        for cust_details,  totalexpenditure in totalmoneyspent.items():
            cust_id, name = cust_details
            print(f'{cust_id}| Name: {name} -> {totalexpenditure}')
            customerspendingreport.append({"Cust_id":cust_id, "Name": name, "Total Expense": totalexpenditure})
        
        self.saveinreport(customerspendingreport)
        
# -----------------------------------------------------------------------------------------------------------        
                
    #question2: category wise spending summary
    def categorywisereport(self):
        categorywisesalesreport = []
        categorycollection = {}
        for transaction in self.transactions:
            categorycollection[transaction[3]] = categorycollection.get(transaction[3], 0) + transaction[4]
            
        for category, totalcollcetion in categorycollection.items():
            print(f' {category} -> {totalcollcetion}')
            categorywisesalesreport.append({'Category': category, 'Collection': totalcollcetion})
            
        self.saveinreport(categorywisesalesreport)
          
 # -----------------------------------------------------------------------------------------------------------         
                    
    #question3: customer ranking
    def rankcustomers(self):
        rankingtosaveinreport = []
        ranking = {}
        for transaction in self.transactions:
            cust_details = (transaction[1],transaction[2])
            ranking[cust_details] = ranking.get(cust_details, 0) + transaction[4]
            
        ranked = sorted(
            ranking.items(),
            key=lambda x: x[1],
            reverse=True
        )
        #this function will sort the dict in descending order on the bases of total expenditure
        
        for rank, ((cust_id, name), total) in enumerate(ranked, start=1):
            print(f'Rank: {rank}| Id: {cust_id}| Name: {name} -> {total} total spendings ')
            rankingtosaveinreport.append({'Rank': rank, 'Id': cust_id, 'Name': name, "Total Spending": total})
            
        self.saveinreport(rankingtosaveinreport)
    
 # -----------------------------------------------------------------------------------------------------------
 
    
    #question4: cashback reward system
    def cashbackdetails(self):
        cashbackrewarddetails = []
        ranking = {}
        for transaction in self.transactions:
            cust_details = (transaction[1],transaction[2])
            ranking[cust_details] = ranking.get(cust_details, 0) + transaction[4]
            
        ranked = sorted(
            ranking.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        print(f'Highest spending customer: {ranked[0][0][1]}')
        print(f'Gets 10% discount\n Total: {ranked[0][1]} \n Discount: {ranked[0][1]*0.1}\n Grand Total: {ranked[0][1]-ranked[0][1]*0.1}')
        print()
        print(f'2nd Highest spending customer: {ranked[1][0][1]}')
        print(f'Gets 5% discount\n Total: {ranked[1][1]} \n Discount: {ranked[1][1]*0.05}\n Grand Total: {ranked[1][1]-ranked[1][1]*0.05}')
        
        
        cashbackrewarddetails.append({'ID': ranked[0][0][0], 'Name': ranked[0][0][1], 'Discount': ranked[0][1]*0.1})
        cashbackrewarddetails.append({'ID': ranked[1][0][0], 'Name': ranked[1][0][1], 'Discount': ranked[1][1]*0.05})
        
        self.saveinreport(cashbackrewarddetails)
            
        
 # -----------------------------------------------------------------------------------------------------------       
        
        
    #question5: customer cupoun retention system
    def cupoundetails(self):
        
        cupoundetailsreport=[]
        ranking = {}
        for transaction in self.transactions:
            cust_details = (transaction[1],transaction[2])
            ranking[cust_details] = ranking.get(cust_details, 0) + transaction[4]
            
        ranked1 = sorted(
            ranking.items(),
            key=lambda x: x[1],
            reverse=False)
        print(f'Lowest spending customer: {ranked1[0][0][1]}\n 10% cupoun awarded\n Cupoun value for this purchase: {ranked1[0][1]*0.1}')
        print(f'2nd Lowest spending customer: {ranked1[1][0][1]}\n 5% cupoun awarded\nCupoun value for this purchase: {ranked1[1][1]*0.05}')
        
        cupoundetailsreport.append({'Name': ranked1[0][0][1], 'Cupoun value': ranked1[0][1]*0.1})
        cupoundetailsreport.append({'Name': ranked1[1][0][1], 'Cupoun value': ranked1[0][1]*0.05})

        self.saveinreport(cupoundetailsreport)
# -----------------------------------------------------------------------------------------------------------


    #question6: multiple same customer transactions
    def counttransactions(self):
        print('Multiple occouring customers: ')
        customer = set()
        for i in range(len(self.transactions)):
            for j in range(i+1, len(self.transactions)):
                if self.transactions[i][1] == self.transactions[j][1]:
                    customer.add((self.transactions[i][1], self.transactions[i][2]))
        
        print(customer)
        
        
# -----------------------------------------------------------------------------------------------------------
        
    #question7: top3 transactions
    def givetop(self, howmany:int):
        ranking = {}
        for transaction in self.transactions:
            cust_details = (transaction[1],transaction[2])
            ranking[cust_details] = ranking.get(cust_details, 0) + transaction[4]
            
        ranked = sorted(
            ranking.items(),
            key=lambda x: x[1],
            reverse=True
        )
        print(f'Top {howmany} Transactions: ')
        for i in range(howmany):
            print(f'Name: {ranked[i][0][1]}| Amount spent: {ranked[i][1]}')
                            
    def searchcustomer(self, cust_id:int):
        print ('Customer transactions: ')
        for transaction in self.transactions:
            if transaction[1]== cust_id:
                print(transaction)
                
# -----------------------------------------------------------------------------------------------------------
    
    #question8: file generation
    def saveinreport(self,thatfile):
        try:
            with open('report.txt', 'r') as file:
                reports = json.load(file)
        except FileNotFoundError:
            reports = []
            
        reports.append(thatfile)
        
        with open('report.txt', 'w') as file:
            json.dump(reports, file)
        
# -----------------------------------------------------------------------------------------------------------      

    def menu(self):
        while True:
            
            print("\n===== RETAIL STORE MENU =====")
            print("1. View Customer Spending Report")
            print("2. View Category Sales Report")
            print("3. Search Customer Transactions")
            print("4. View Cashback Rewards")
            print("5. View Coupon Details")
            print("6. Generate Reports")
            print("7. Exit")
            
            choice = int(input('Enter your input: '))
            if choice == 1:
                self.spendingsummary()

            elif choice == 2:
                self.categorywisereport()

            elif choice == 3:
                cust_id = int(input("Enter Customer ID: "))
                self.searchcustomer(cust_id)

            elif choice == 4:
                self.cashbackdetails()

            elif choice == 5:
                self.cupoundetails()

            elif choice == 6:
                with open('report.txt', 'r') as file:
                    data = json.load(file)
                print(data)

            elif choice == 7:
                print("Thank you for using Retail Store System!")
                break

            else:
                print("Invalid choice. Please try again.")
  
if __name__=='__main__':
    
    rs = retailstoreas()
    # rs.insertinitialdata(transactionslist)
    # rs.appenddata(9,5,'Yatesh', 'Travel', 25000)
    # rs.appenddata(10,5,'Yatesh', 'Food', 2000)
    # rs.removetransaction(9)
    # rs.spendingsummary()
    # rs.categorywisereport()
    # rs.rankcustomers()
    # rs.cashbackdetails()
    # rs.cupoundetails()
    # rs.counttransactions()
    # rs.givetop(3)
    # rs.searchcustomer(5) 
    rs.menu()
 

