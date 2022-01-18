import math

def grader(score):
    grades = 'ABCDFFFFFF'
    if score > 0:
        return grades[10 - math.ceil(score/10)]
    else:
        return 'F'
    
x = float(input("Enter your score -> "))
print(f"Your grade is {grader(x)}")