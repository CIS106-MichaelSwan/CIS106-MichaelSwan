#input phase
firstname = input("Enter your first name: ")
steps = input("Enter the number of steps you walked today: ")

#process phase
caloriesburned = int(steps) * 0.25
#output phase
print(firstname + ", you burned " + str(caloriesburned) + " calories today.")