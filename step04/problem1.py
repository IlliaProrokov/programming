# Name: Illia Prorokov


for number in range(1, 11):
    print(number)





# Problem 2: Count to 10 with a while loop

number = 1
while number <= 10:
    print(number)
    number = number + 1




# Problem 3: Even numbers

for number in range(2, 21, 2):
    print(number)



# Problem 4: Add up 1 to 100

total = 0
for number in range(1, 101):
    total = total + number

print(f"The total is {total}")




# Problem 5: Password checker

PASSWORD = "python123"

guess = input("Enter the password: ")
while guess != PASSWORD:
    print("Try again!")
    guess = input("Enter the password: ")

print("Access granted!")



# Problem 6: Times table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")





# Problem 7: Add numbers until zero

total = 0
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    total = total + number
    number = int(input("Enter a number (0 to stop): "))

print(f"The total is {total}")





# Problem 8: Countdown

start = int(input("Count down from: "))

for number in range(start, 0, -1):
    print(number)

print("Liftoff!")





# Problem 9: Positive or negative

number = int(input("Enter a number (0 to stop): "))

while number != 0:
    if number < 0:
        print("Negative")
    else:
        print("Positive")
    number = int(input("Enter a number (0 to stop): "))

print("All done.")



# Name: Your Name
# Date: November 17, 2026
# Program: step04_p10.py - Average of five test scores

total = 0

for i in range(5):
    score = float(input("Test score: "))
    total = total + score

average = total / 5
print(f"Average: {average:.1f}")





#Problem 11: Ask again until it is in range
rating = int(input("Rate the movie (1-10): "))

while rating < 1 or rating > 10:
    print("Please enter 1 to 10.")
    rating = int(input("Rate the movie (1-10): "))

print(f"Your rating: {rating}")




#Problem 12: Star bar

name = input("Player name: ")
points = int(input("Points scored: "))

bar = ""
for i in range(points):
    bar = bar + "*"

print(f"{name}: {bar}")


#Problem 13: Count and add until zerocount = 0
total = 0

number = int(input("Enter a number (0 to stop): "))
while number != 0:
    count = count + 1
    total = total + number
    number = int(input("Enter a number (0 to stop): "))

print(f"You entered {count} numbers.")
print(f"The total is {total}")











#Challenge: Class Score Summary

PASSING_SCORE = 70

# Input
students = int(input("How many students? (1-30): "))
while students < 1 or students > 30:
    print("Please enter 1 to 30.")
    students = int(input("How many students? (1-30): "))

total = 0
passing = 0

for student in range(1, students + 1):
    score = float(input(f"Score for student {student}: "))
    while score < 0 or score > 100:
        print("Scores must be 0 to 100.")
        score = float(input(f"Score for student {student}: "))

    # Processing
    total = total + score
    if score >= PASSING_SCORE:
        passing = passing + 1

average = total / students

chart = ""
for i in range(passing):
    chart = chart + "#"

if passing == 0:
    chart = "none"

# Output
print()
print("--- Class Summary ---")
print(f"Students:  {students}")
print(f"Average:   {average:.1f}")
print(f"Passing:   {passing}")
print(f"Chart:     {chart}")





