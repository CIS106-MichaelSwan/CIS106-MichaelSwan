def CompPayRate(JobCode):
  if JobCode == "L":
    PayRate = 25
  elif JobCode == "A":
    PayRate = 30
  elif JobCode == "J":
    PayRate = 50
  else:
    PayRate = 0
  return PayRate
def CompGrossPay(PayRate, Hours):
  if Hours > 40:
    GrossPay = PayRate * 40 + (1.5 * PayRate * (Hours - 40))
  else:
    GrossPay = PayRate * Hours
  return GrossPay
TotalGrossPay = 0
r = input(str("Do you want to calculate gross pay? (Yes or No): "))
while r == "Y":
  LastName = input(str("Enter last name: "))
  JobCode = input(str("Enter job code: "))
  Hours = float(input("Enter hours worked: "))
  PayRate = CompPayRate(JobCode)
  GrossPay = CompGrossPay(PayRate, Hours)
  TotalGrossPay = TotalGrossPay + GrossPay
  print("Last name: ", LastName)
  print("Gross pay: $", GrossPay)
  r = input("Do you want to calculate gross pay? (Yes or No): ")
print("Total Gross Pay is $", TotalGrossPay)