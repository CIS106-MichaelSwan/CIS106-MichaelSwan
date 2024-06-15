#input phase
Make = input("Enter the make of the car: ")
Model = input("Enter the model of the car: ")
msrp = float(input( "Enter the msrp of the car: "))
discount = float(input("Enter the discount percentage: "))

#process phase
amountoff = msrp * discount
discountedprice = msrp - amountoff

#output phase
print("Make: ", Make)
print("Model: ", Model)
print("MSRP: ", msrp)
print("Discount Percentage: ", discount)
print("Amount Off: ", amountoff)
print("Discounted Price: ", discountedprice)