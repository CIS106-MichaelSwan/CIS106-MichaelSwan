def discount(qty, price, discrate):
    total = (qty * price)
    discamt = discrate * total
    discprice = total - discamt
    
    return discamt,discprice




qty = float(input("Enter quantity: "))
price = float(input("Enter price: "))
discrate = float(input("Enter discount rate: "))
discamt,discprice = discount(qty, price, discrate)
print("This is your quanity: ", qty)
print("This is your price: ", price)
print("This is your discounted amount" , discamt)
print("This is your discounted price" , discprice)
