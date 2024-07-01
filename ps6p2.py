#input phase
partno = int(input("Enter part number: "))
quantity = int(input("Enter quantity: "))
#process phase
if partno == 10 or partno == 55:
  unitprice = 1.00
elif partno == 99:
  unitprice = 2.00
elif partno == 80 or partno == 70:
  unitprice = 3.00
else:
  unitprice = 5.00

total = float(quantity) * unitprice
#print phase
print(f"Part number: {partno}")
print(f"Unit price: ${unitprice}")
print(f"Total: ${total}")
