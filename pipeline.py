from functools import reduce

transactions =[ {"id": 1, "amount": 100, "type": "debit", "category": "food"},
    {"id": 2, "amount": 200, "type": "credit", "category": "salary"},
    {"id": 3, "amount": 110, "type": "credit", "category": "salary"},
    {"id": 4, "amount": 250, "type": "debit", "category": "salary"},
    {"id": 5, "amount": 500, "type": "debit", "category": "salary"}]

debits = list(filter(lambda items : items['type'] == 'debit', transactions))

amounts = list(map(lambda items : {"amount" : items['amount']}, debits))

total = reduce(lambda x, y: x + y['amount'] , amounts, 0)
print(total)