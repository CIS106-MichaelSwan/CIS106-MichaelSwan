#input phase
mealtotal = float(input("Enter the total amount of the meal: "))


#process phase
tip1 = mealtotal * .15
tip2 = mealtotal * .18
tip3 = mealtotal * .20
value1 = mealtotal + tip1
value2 = mealtotal + tip2
value3 = mealtotal + tip3
#output phase
print("With 15% Tip:")
print("The total amount of the meal is: ", mealtotal)
print( "The tip amount at 15% is: ", tip1)
print( "The total amount with the tip is: ", value1)
print("With 18% Tip:")
print("The total amount of the meal is: ", mealtotal)
print( "The tip amount at 18% is: ", tip2)
print( "The total amount with the tip is: ", value2)
print("With 20% tip:")
print("The total amount of the meal is: ", mealtotal)
print( "The tip amount at 20% is: ", tip3)
print( "The total amount with the tip is: ", value3)