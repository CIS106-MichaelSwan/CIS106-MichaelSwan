totalextprice = 0
totalorders = 0
response = input("Would you like to run the program? (yes/no): ")
while response == "yes":
  item = input( "Enter an item: ")
  qty = input( "Enter the quantity: ")
  price = input( "Enter the price: ")
  extprice = float(qty) * float(price)
  print( "Item: " + item)
  print( "Quantity: " + qty)
  print( "Price: " + price)
  print( "Extended Price: " + str(extprice))
  totalextprice = totalextprice + extprice
  totalorders = totalorders + 1 
  avgorderprice = totalextprice / totalorders
  response = input("Would you like to calculate item price? (yes/no): ")


print("Total Extended Price: ", totalextprice)
print("Total Number of Orders:" , totalorders)
print("Average Order Price: ", avgorderprice)