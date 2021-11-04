import classes

Stock_One = classes.Stock(1070, 1000000000, 'US88160R1014', 20)

print('Stock price:', Stock_One.price)
print('Amount:', Stock_One.amount)
splitfactor=3

Stock_One.stocksplit(splitfactor)

print('Price after split by factor',splitfactor,':', Stock_One.price)
print('Amount after split:', Stock_One.amount)


My_Gold = classes.Gold(500, 8000000, 'highest', 4)

print('I have', My_Gold.amount, 'ounces of gold worth', My_Gold.amount*My_Gold.price, 'USD')