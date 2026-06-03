authorized_users = [1, 2, 3, 4, 5]
requested_users = [2, 3,7,5]
for char in requested_users:
    if char in authorized_users:
        print(f'{char} is authorized user. access granted')
    else:
        print(f'Access denied for user {char}')
