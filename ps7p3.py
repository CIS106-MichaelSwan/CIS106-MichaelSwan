response = input("Want to calculate average score? (yes or no):")

while response == "yes":
  lastname = input("Enter last name:")
  score1 = float(input("Enter exam score 1:"))
  score2 = float(input("Enter exam score 2:"))
  avg = (score1 + score2) / 2
  print("Last name:", lastname)
  print("Average score:", avg)
  response = input("Want to calculate average score? (yes or no):")