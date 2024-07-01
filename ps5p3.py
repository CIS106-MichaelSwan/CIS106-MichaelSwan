#input phase
numberofbooks = float(input("Enter the number of books: "))
bookcost = float(input("Enter the cost of each book: "))
#process phase
ordertotal = numberofbooks * bookcost

if ordertotal > 50.00:
  shipping = 0.00
else:
  shipping = 25.00

#input phase
print("Order total: ", ordertotal)
print("Shipping: ", shipping)