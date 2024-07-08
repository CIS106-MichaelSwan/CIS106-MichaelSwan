totaldiscount = 0
response = input("Want to calculate total order with discount? (yes/no)")

while response == "yes":
  qty = float(input("Enter quantity: "))
  price = float(input("Enter price: "))
  extprice = qty * price
  if extprice > 10000.00:
    discount = extprice * 0.25
  else:
    discount = extprice * 0.10
  discprice = extprice - discount
  totaldiscount = totaldiscount + discount
  print("Extended price: $", extprice)
  print("Discount amount: $", discount)
  print("Discounted price: $", discprice)
  response = input("Want to calculate another order? (yes/no)")
  #response = "yes" 
  #break  
print("Total discount amount: $", totaldiscount)