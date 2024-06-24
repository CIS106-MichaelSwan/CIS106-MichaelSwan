#input phase
fixedcosts = float(input("Enter fixed costs: "))
priceperunit = float(input("Enter price per unit: "))
costperunit = float(input("Enter cost per unit: "))

#process phase
breakevenpoint = fixedcosts / (priceperunit - costperunit)
#output phase
print(f"The break even point is {breakevenpoint}")