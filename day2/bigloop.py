

number_of_grades = int(input())
count = 0
sum_of_grades = 0

while count < number_of_grades:
    # ask for a another grade
    grade = float(input())
    sum_of_grades = sum_of_grades + grade

    # increment count
    count = count + 1

average = sum_of_grades / number_of_grades
print(average)