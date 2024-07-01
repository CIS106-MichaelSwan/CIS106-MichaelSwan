#input phase
lastname = input("Enter last name: ")
grosspay = float(input("Enter gross pay: "))
nodep = float(input("Enter number of dependents: "))

#process phase
adjgross = grosspay - (nodep * 12000)

if adjgross > 50000:
  taxrate = 0.2 * adjgross
else:
  taxrate = 0.1 * adjgross

if taxrate < 0:
  taxrate = 100

#output phase
print(lastname)
print("Gross Income: $", grosspay)
print( "Number of dependents: ", nodep)
print("Adjusted Gross Income: $", adjgross)
print( "Income Tax: $", taxrate)