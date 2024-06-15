#input phase
amount = float(input("Enter the amount paid for job: "))
distribution = float(input("Enter the number of people that completed the job: "))

#process phase
amountpaid = amount / distribution

#output phase
print("Each person will get: ", amountpaid)