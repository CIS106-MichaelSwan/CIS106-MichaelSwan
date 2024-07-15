def CompTuitionOwed(DistrictCode, Credits):
  if DistrictCode == "I":
    TuitionOwed = float(Credits) * 250.00
  else:
    TuitionOwed = float(Credits) * 550.00
  return TuitionOwed
TotalTuition = 0 
r = input("Do you want to calculate tuition? (Y/N): ")
while r == "Y":
  LastName = input("Enter student last name: ")
  DistrictCode = input("Enter district code (I or O): ")
  Credits = input("Enter number of credits: ")
  TuitionOwed = CompTuitionOwed(DistrictCode, Credits)
  print("Student last name: ", LastName)
  print("Tuition owed: $", TuitionOwed)
  TotalTuition = TotalTuition + TuitionOwed
  r = input("Do you want to calculate tuition? (Y/N): ")
print("Total tuition owed: $", TotalTuition)