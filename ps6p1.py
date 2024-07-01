#input phase
quantityofwidgets = float(input("Enter the quantity of widgets: "))

#process phase
if quantityofwidgets > 10000:
  price = 10
elif quantityofwidgets >= 5000 and quantityofwidgets <= 10000:
  price = 20
else:
  price = 30

extendedprice = quantityofwidgets * price
taxamount = extendedprice * 0.07
#print phase
print("Extended price $", extendedprice)
print("Tax amount $", taxamount)
print( "Total $", extendedprice + taxamount)
