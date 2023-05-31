transactions = {
    'a':{'id': 1, 'date': '2024-05-20 12:02:50', 'amount': 100, 'status': 'pending', 'customer': {'name': 'yasnoslava', 'email': 'ysnhn@gmail.com', 'phone': '+380997832498'}},
    'b':{'id': 2, 'date': '2024-11-26 16:32:50', 'amount': 10, 'status': 'completed', 'customer': {'name': 'olha', 'email': 'olha@gmail.com', 'phone': '+380997832345'}},
    'c':{'id': 3, 'date': '2024-09-21 18:14:52', 'amount': 300, 'status': 'failed', 'customer': {'name': 'pavlo', 'email': 'pavlo@gmail.com', 'phone': '+380997837709'}},
    'd':{'id': 4, 'date': '2024-09-21 18:14:52', 'amount': 300, 'status': 'failed', 'customer': {'name': 'pavlo', 'email': 'pavlo@gmail.com', 'phone': '+380997837709'}},
    'e':{'id': 5, 'date': '2024-11-26 16:32:50', 'amount': 10, 'status': 'completed', 'customer': {'name': 'olha', 'email': 'olha@gmail.com', 'phone': '+380997832345'}}
}

# 3
for i in transactions:
    print(transactions[i], '\n')
    
# 4
transactions['a']['status'] = 'completed'

# 5
del transactions["e"]

# 6
for user in transactions:
    print(transactions[user]['id'], end = ', ')
print('\n')

# 7
customers = {}
for el in transactions:
    key = transactions[el]['customer']['name']
    if key in customers:
        customers[key].append(transactions[el]['id'])
    else:
        customers[key] = []
        customers[key].append(transactions[el]['id'])
# print(customers)

# 8
for i in customers:
    print(f'платник: {i}; id: {customers[i]}')