#input phase
principleamountofcd = float(input("Enter the principle amount of the CD: "))
yeartomaturity = int(input("Enter the year to maturity of the CD: "))

#process phase
if principleamountofcd > 100000 and yeartomaturity == 5:
  intrate = 0.06
elif principleamountofcd >= 50000 and principleamountofcd <= 100000 and yeartomaturity == 10:
  intrate = 0.05
elif principleamountofcd >= 50000 and principleamountofcd <= 100000 and yeartomaturity == 5:
  intrate = 0.04
else:
   intrate = 0.02

firstyearinterest = principleamountofcd * intrate
#print phase
print("Principle: " + str(principleamountofcd))
print("Interest rate: " + str(intrate))
print("Interest amount for the first year: " + str(firstyearinterest))
