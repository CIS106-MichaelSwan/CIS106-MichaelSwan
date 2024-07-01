#input phase
quantity = float(input("Enter the quantity of the item: "))


#process phase
if quantity >= 1000:
  unitprice = 3.00
else:
  unitprice = 5.00

extprice = quantity * unitprice
tax = extprice * 0.07
total = extprice + tax
#output phase
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unitprice:.2f}")
print(f"Extended Price: ${extprice:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")