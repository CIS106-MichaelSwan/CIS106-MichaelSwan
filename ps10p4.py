def CompTrainTicket(Miles):
  if Miles >= 30:
    TicketPrice = 12
  else:
    if Miles >= 20:
      TicketPrice = 10
    else:
      if Miles >= 10:
        TicketPrice = 8
      else:
        TicketPrice = 5
  return TicketPrice
TotalTicketPrice = 0 
r = input("Do you want to run the program? (y/n): ")
while r == "y":
  LastName = input("Enter your last name: ")
  Miles = float(input("Enter the number of miles from downtown Chicago: "))
  TicketPrice = CompTrainTicket(Miles)
  TotalTicketPrice = TotalTicketPrice + TicketPrice
  print("The ticket price is $", TicketPrice)
  r = input("Do you want to run the program again? (y/n): ")
print("The sum of all ticket prices is $", TotalTicketPrice)