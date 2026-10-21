"""inventory_items = ['Frozen Ham', 'Frozen Turkey', 'Canned Yams', 'Canned Corn', 'Canned Green beans',
             'Canned Carrots', 'Canned Peas', 'Canned Fruit', 'Canned Pumpkin', 'Canned Milk',
             'Instant Mashed Potatoes', 'Potatoes', 'Sugar', 'Flour', 'Cranberry Sauce',
             'Pie Crust', 'Pie Filling', 'Stuffing Mix', 'Gravy Mix', 'Bread mix', 'Cookie Mix',
             'Cake Mix and Icing', 'Cooking Oil', 'Mac n Cheese']"""

inventory = 'inventory.txt'
transactions = 'transactions.txt'

with open (inventory, 'w') as file:
    inventory = file.write('testing again')
    print('inventory is open')


"""Plan for any futuer ideas to combine both of these to reduce line count and consider weather
it will make things faster and easier to read"""

with open (transactions, 'w') as file:
    transactions = file.write('testing 2 again')
    print('transactions is open')
