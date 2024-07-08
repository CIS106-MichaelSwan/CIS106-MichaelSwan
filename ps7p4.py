employee = 0 
totalgross = 0
response = input("Want to calculate gross pay? (yes/no)")

while response == "yes":
  lastname = input("Enter Last Name:")
  hours = int(input("Enter hours worked: "))
  rate = int(input("Enter hourly rate:"))
  if hours >= 40:
    gross = ((hours - 40) * (rate * 1.5)) + (40 * rate)
  else:
    gross = rate * hours
  print("Last Name:" + lastname)
  print ("Gross pay is: ", gross)
  totalgross = totalgross + gross
  employee = employee + 1
  response = input("Want to calculate gross pay? (yes/no)")
  #response = "yes" 
  #break  
  averagegross = totalgross / employee
  print("Total gross pay is: ", totalgross)
  print("Number of employees is: ", employee)
  print("Average gross pay is: ", averagegross)