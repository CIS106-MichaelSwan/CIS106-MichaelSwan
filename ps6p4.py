#input phase
numberofconcerttickets = float(input("Enter the number of concert tickets: "))
#process phase
if numberofconcerttickets >= 25:
  priceperticket = 50
elif numberofconcerttickets >= 10 and numberofconcerttickets <= 24:
  priceperticket = 60
elif numberofconcerttickets >= 5 and numberofconcerttickets <= 9:
  priceperticket = 70
elif numberofconcerttickets < 5:
  priceperticket = 75

totalcost = numberofconcerttickets * priceperticket

#output phase
print("The number of concert tickets: ", numberofconcerttickets)
print("The price per ticket: $", priceperticket)
print("The total cost: $", totalcost)

