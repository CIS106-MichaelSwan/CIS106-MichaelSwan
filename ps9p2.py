def CompBatAvg(hits, atBats):
  BatAvg = hits / atBats
  return BatAvg
TotalPlayers = 0
r = input("Do you want to calculate batting average? (Y/N):")
while r == "Y":
  name = input("Enter last name:")
  hits = float(input("Enter number of hits:"))
  atBats = float(input("Enter at bats:"))
  BatAvg = CompBatAvg(hits, atBats)
  print(name, "has batting average of", BatAvg)
  TotalPlayers = TotalPlayers + 1
  r = input("Do you want to calculate batting average? (Y/N)")
print("Number of players:", TotalPlayers)