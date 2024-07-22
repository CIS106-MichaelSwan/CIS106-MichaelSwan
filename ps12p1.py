def displayarrays(LastName):
  for i in range (0, 10, 1):
    print(LastName[i])

def rdisplayarrays(LastName):
  for i in range (9, -1, -1):
    print(LastName[i])

LastName = ["Adams", "Baker", "Smith", "Davis", "Jones", "Kelly", "Williams", "Cook", "Brown", "Jones"]

displayarrays(LastName)
rdisplayarrays (LastName)
print(LastName)
LastName2 = LastName[::-1]
print(LastName2)
LastName.reverse()