def CompForecast(month, sales):
  if month == "1" or month == "2" or month == "3":
    forecast = 0.10
  elif month == "4" or month == "5" or month == "6":
    forecast = 0.15
  elif month == "7" or month == "8" or month == "9":
    forecast = 0.20
  else:
    forecast = 0.25
  nextmonth = int(month) + 1
  nextmonthsales = sales * (1 + forecast)
  return nextmonth, nextmonthsales
r = input("Do you want to run the program? (y/n): ")
while r == "y":
  LastName = input("Enter salesperson's last name: ")
  Month = int(input("Enter Month (as a number, e.g., 1 for January): "))
  Sales = float(input("Enter sales amount: "))
  nextmonth, nextmonthsales = CompForecast(Month, Sales)
  print("Next month is", nextmonth, "and the sales will be", nextmonthsales)
  r = input("Do you want to run the program again? (y/n): ")

