def CompAssessedValue(County, MarketValue):
  if County == "Cook":
    AssessedValue = MarketValue * 0.90
  elif County == "DuPage":
    AssessedValue = MarketValue * 0.80
  elif County == "McHenry": 
    AssessedValue = MarketValue * 0.75
  elif County == "Kane":  
    AssessedValue = MarketValue * 0.60  
  else:
    AssessedValue = MarketValue * 0.70
  return AssessedValue # Add the return statement here

TotalMarketValue = 0
TotalAssessedValue = 0
r = input("Do you want to run the program? (Y or N): ")
while r == "Y":
  County = input("Enter the county: ")
  MarketValue = float(input("Enter the market value: "))
  AssessedValue = CompAssessedValue(County, MarketValue)
  TotalMarketValue = TotalMarketValue + MarketValue
  TotalAssessedValue = TotalAssessedValue + AssessedValue
  print("Market Value: $", MarketValue)
  print("Assessed Value: $", AssessedValue)  
  r = input("Do you want to run the program again? (Y or N): ")
print("Total Market Value: $", TotalMarketValue) 
print("Total Assessed Value: $", TotalAssessedValue)