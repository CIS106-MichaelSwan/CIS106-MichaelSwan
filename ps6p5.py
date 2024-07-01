#input phase
employeelastname = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
joblevel = float(input("Enter job level: "))
#process phase
if joblevel >= 10:
  bonusrate = 0.25
elif joblevel >= 5 and joblevel <= 9:
  bonusrate = 0.20
else:
  bonusrate = 0.10

bonus = salary * bonusrate
#output phase
print("Employee last name: ", employeelastname)
print("Bonus: $", bonus)

