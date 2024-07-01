#input phase
name = input("Enter Appliance Name: ")
cost = float(input("Enter Cost of Appliance: "))
#process phase
if cost > 1000:
  warrantee = cost * 0.1
else: 
  warrantee = cost * 0.05

totalcost = cost + warrantee
#input phase
print("Name: ", name)
print( "Cost: ", cost)
print( "Warranty cost: ", warrantee)
print( "Total Cost: ", totalcost)