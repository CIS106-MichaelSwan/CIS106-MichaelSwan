def CompSquareFootage(length, width, wall1length, wall1height, wall2length, wall2height, ceilinglength, ceilingwidth, floorlength, floorwidth):
  ceiling_area = 2 * floorlength * ceilingwidth
  wall1_area = 2 * wall1length * wall1height
  wall2_area = 2 * wall2length * wall2height
  SquareFootage = ceiling_area + wall1_area + wall2_area
  return SquareFootage
r = input("Do you want to run the program? (y/n): ")
while r == "y":
  length = float(input("Enter the length of the room: "))
  width = float(input("Enter the width of the room: "))
  height = float(input("Enter the height of the room: "))
  wall1length = float(input("Enter the length of the first wall: "))
  wall1height = float(input("Enter the height of the first wall: "))
  wall2length = float(input("Enter the length of the second wall: "))
  wall2height = float(input("Enter the height of the second wall: "))
  ceilinglength = float(input("Enter the length of the ceiling: "))
  ceilingwidth = float(input("Enter the width of the ceiling: "))
  floorlength = float(input("Enter the length of the floor: "))
  floorwidth = float(input("Enter the width of the floor: "))
  SquareFootage = CompSquareFootage(length, width, wall1length, wall1height, wall2length, wall2height, ceilinglength, ceilingwidth, floorlength, floorwidth)
  Gallons = SquareFootage / 50
  print("The square footage of the room is: ", SquareFootage)
  print("The number of gallons of paint needed is: ", Gallons)
  r = input("Do you want to run the program again? (y/n): ")