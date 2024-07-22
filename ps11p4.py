def bowlingavg(score1, score2, score3, handicap):
    sum = score1 + score2 + score3
    avg = sum / 3
    handicapavg = (sum + handicap) / 3
    return avg, handicapavg



lastname = str(input("Enter last name: "))
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
handicap = float(input("Enter handicap: "))
avg, handicapavg = bowlingavg(score1, score2, score3, handicap)
print("Last name: ", lastname)
print("Average score: ", avg)
print("Handicap average score: ", handicapavg)
            