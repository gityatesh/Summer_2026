messages = [
("Rahul","Hi"),
("Aman","Hello"),
("Rahul","How are you?"),
("Aman","Good Morning"),
("Rahul","Let's meet")
]

convo_history = {}
for user, msgs in messages:
    convo_history.setdefault(user, []).append(msgs)
    
print(convo_history)