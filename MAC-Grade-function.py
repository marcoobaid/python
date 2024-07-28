score = input("Enter a grade: ")

def computegrade(x):
    if x >= 0.9 and x <= 1.0:
        grade = "A"
    elif x < 0.9 and x >= 0.8:
        grade = "B"
    elif x < 0.8 and x >= 0.7:
        grade = "C"
    elif x < 0.7 and x >= 0.6:
        grade = "D"
    elif x < 0.6 and x >= 0:
        grade = "F"
    else:
        quit()  
    return grade

try:
    score = float(score)
    grade = computegrade(score)
    print(grade)
except:
    print("Bad Score")