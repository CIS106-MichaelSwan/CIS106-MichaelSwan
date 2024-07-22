def exam_average(exam1, exam2, exam3):
    sum = exam1 + exam2 + exam3
    total = 300   
    percentage = (sum / total) * 100
    average = sum / 3
    points = exam1 + exam2 + exam3
    return average, points



lastname = str(input( "Enter your last name: "))
exam1 = float(input( "Enter your first exam score: "))
exam2 = float(input( "Enter your second exam score: "))
exam3 = float(input( "Enter your third exam score: "))

average, points = exam_average(exam1, exam2, exam3)
print("Last name: ", lastname)
print("Average exam score: ", average)
print("Total points earned: ", points)

