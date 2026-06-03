# functions on list
transactions = [
("food", 200),
("travel", 500),
("food", 100),
("shopping", 1000),
("travel", 300)
]
# expencesforfood=0
# expencesfortravel=0
# expencesforshopping=0
# for i in transactions:
#     if(i[0]=='food'):
#         expencesforfood+=i[1]
#     if(i[0]=='travel'):
#         expencesfortravel+=i[1]
#     if(i[0]=='shopping'):
#         expencesforshopping += i[1]
        
# print(expencesforfood, expencesforshopping, expencesfortravel)


summary = {}

for category, amount in transactions:
    summary[category] = summary.get(category,0) + amount #summary.get directly call the naem of the service
    
print(summary)