def CompExtPrice(qty, unitprice):
  extprice = qty * unitprice

  if extprice > 10000.00:
    discamt = extprice * 0.10
  else:
    discamt = 0.0

  return extprice

totalextprice = 0.0
r = input("Do you want to calculate the total order ext price? (yes or no):")

while r == "yes":
  qty = float(input("Enter the quantity:"))
  unitprice = float(input("Enter the unit price:"))
  extprice = CompExtPrice(qty, unitprice)
  totalextprice = totalextprice + extprice
  print("The extended price is $", extprice)
  print("The quantity is", qty)
  r = input("Do you want to calculate the total order ext price? (yes or no):")
print("Total Extended Price is $", totalextprice)