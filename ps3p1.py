#input phase
stocksymbol = input("Enter the stock symbol: ")
shares = float(input("Enter the number of shares: "))
costpershare = float(input("Enter the cost per share: "))

#process phase
amountinvested = shares * costpershare

#output phase
print(f"Amount invested: ${amountinvested:,.2f}")
print(f"Stock Symbol: {stocksymbol}")