# Name: Illia Prorokov
# Problem 1: A welcome banner

def print_banner():
    print("=" * 20)
    print("  BPA Python Club")
    print("=" * 20)


print_banner()
print_banner()



#Problem 2: Greet three people
def greet(name):
    print(f"Hello, {name}! Welcome to class.")


greet("Avery")
greet("Blake")
greet("Casey")


# Problem 3: Square numbers
def square(number):
    return number * number


for num in range(1, 6):
    print(f"{num} squared is {square(num)}")


# Problem 4: Average of three
def average_of_three(a, b, c):
    return (a + b + c) / 3


score1 = float(input("Score 1: "))
score2 = float(input("Score 2: "))
score3 = float(input("Score 3: "))

average = average_of_three(score1, score2, score3)
print(f"Average: {average:.1f}")




# Problem 5: Even or odd
def is_even(number):
    return number % 2 == 0


num = int(input("Enter a number: "))

if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")




#Problem 6: Letter grade
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


student_score = float(input("Score: "))
print(f"Letter grade: {letter_grade(student_score)}")



# Problem 7: Tip calculator
def calculate_tip(bill, percent):
    return bill * (percent / 100)


bill_amount = float(input("Bill amount: "))
tip_percent = int(input("Tip percent: "))

tip = calculate_tip(bill_amount, tip_percent)
total = bill_amount + tip

print(f"Tip:   ${tip:.2f}")
print(f"Total: ${total:.2f}")




#Problem 8: A line of any length

def print_line(symbol, length):
    line = ""
    for i in range(length):
        line = line + symbol
    print(line)


print_line("*", 10)
print_line("-", 15)
print_line("#", 5)




# Problem 9: Rectangle area and perimeter

def calculate_perimeter(width, height):
    return 2 * (width + height)


rect_width = float(input("Width: "))
rect_height = float(input("Height: "))

area = calculate_area(rect_width, rect_height)
perimeter = calculate_perimeter(rect_width, rect_height)

print(f"Area:      {area}")
print(f"Perimeter: {perimeter}")




#Problem 10: Temperature table
def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


print("Celsius  Fahrenheit")
for celsius in range(0, 101, 20):
    fahrenheit = to_fahrenheit(celsius)
    print(f"{celsius:<9}{fahrenheit:.1f}")



    #Problem 11: Bigger of two
def bigger(a, b):
    if a > b:
        return a
    else:
        return b


first = int(input("First number: "))
second = int(input("Second number: "))

print(f"The bigger number is {bigger(first, second)}")




# Problem 12: Use main()
def calculate_total(price, quantity):
    return price * quantity


def main():
    item = input("Item: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    total = calculate_total(price, quantity)
    print(f"{quantity} {item} cost ${total:.2f}")


if __name__ == "__main__":
    main()
