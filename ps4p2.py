#input phase
pricepershare = float(input("Enter price per share: "))
currentprice = float(input("Enter current price: "))
quantity = float(input("Enter quantity: "))


#process phase
value = (currentprice - pricepershare) * quantity

#output phase
print("The value of the stock is $", value)