def CompMpg(Miles, Gallons):
  Mpg = Miles / Gallons
  return Mpg
TotalTrips = 0
r = input("Do you have a trip to record? (y/n):")
while r == "Y":
  City = input("Enter the destination city:")
  Miles = float(input("Enter the number of miles:"))
  Gallons = float(input("Enter the number of gallons:"))
  Mpg = CompMpg(Miles, Gallons)
  print("The destination city is:", City)
  print("The miles per gallon is:", Mpg)
  print("The miles traveled was:", Miles)
  TotalTrips = TotalTrips + 1
  r = input("Do you have a trip to record? (y/n):")
print("Number of Trips:", TotalTrips)