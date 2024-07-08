response = input("Do you want to calculate interest? (yes/no):")
while response == "yes":

  p = float(input("Enter Principle Amount:"))
  i = float(input("Enter Interest Rate:"))

  totint= 0.0 

  print("Year", "    Beg Balance  ", "  End Balance    ")
  for count in range (1,6,1):
    intamt = p * i
    totint = totint + intamt
    endbal = p + intamt
    print(count,"       ", p,"      ", endbal)
    p = endbal
  response = input("Do you want to calculate interest? (yes/no):")

print("Total Interest Earned: ", totint)