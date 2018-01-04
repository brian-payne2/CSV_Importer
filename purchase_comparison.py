# import statements
import csv
import pprint

# global variables
purchases = {}
f_purchases = {}
product_list = []

# determine if each line has been added to the list of purchases
with open('dummy.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['purchase_id'] not in purchases:
			purchases[row['purchase_id']] = []
		purchases[row['purchase_id']].append(row['product_id'])

# filter out single item purchases
for key in purchases:
    if len(purchases[key]) > 1:
        f_purchases[key] = purchases[key]
pprint.pprint(f_purchases)
