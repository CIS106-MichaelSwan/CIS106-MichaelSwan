numberofstudents = 0
totaltuition = 0 
response = input("Would you like to run the program? (yes/no): ")
while response == "yes":
  lastname = input("Enter your last name: ")
  creditstaken = float(input("Enter the number of credits taken this semester: "))
  districtcode = input("Enter your district code (I or O): ")
  if districtcode == "I":
    costpercredit = 250
  else:
    costpercredit = 500
  tuitionowed = costpercredit * creditstaken
  print("Last name: ", lastname)
  print("Credits taken: ", creditstaken)
  print("Tuition owed: $", tuitionowed)
  numberofstudents = numberofstudents + 1
  totaltuition = totaltuition + tuitionowed
  response = input("Would you like to run the program again? (yes/no): ")

print("Number of students: ", numberofstudents)
print("Total tuition owed: $", totaltuition)