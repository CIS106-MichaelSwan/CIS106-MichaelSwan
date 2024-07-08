totalbonus = 0
response = input("Would you like to calculate bonus? (yes/no): ")
while response == "yes":
   lastname = input("Enter last name: ")
   salary = int(input("Enter salary: "))
   bonus = 0  # Initialize bonus outside the loop
   if salary >= 100000.00:
     bonus = salary * 0.20
   elif salary >= 50000.00:
     bonus = salary * 0.15
   else:
     bonus = salary * 0.10
   totalbonus = totalbonus + bonus
   print(lastname)
   print(salary)
   print(bonus)
   response = input("Would you like to calculate bonus? (yes/no): ")

print("Total Bonus: ", totalbonus)