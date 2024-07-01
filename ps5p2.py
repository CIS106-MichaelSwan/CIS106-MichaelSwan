#input phase
item = input("Enter item (A or B): ")
quantity = float(input("Enter quantity: "))


#process phase
if item == "A":
  unitprice = 10.00
else:
  unitprice = 20.00

extprice = unitprice * quantity
#output phase
print("Item: ", item)
print( "Unit price: $", unitprice)
print("Extended price: $", extprice)