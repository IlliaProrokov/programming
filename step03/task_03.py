# Author: Illia Prorokov
# Description: Calculates the price of a movie ticket based on age, day, and 3D option.

CHILD_PRICE = 7.00
ADULT_PRICE = 11.00
SENIOR_PRICE = 8.00
TUESDAY_DISCOUNT = 3.00
THREE_D_CHARGE = 2.50

# Input
name = input("Name: ")
age = int(input("Age: "))
day = input("Day of the week: ")
three_d = input("3D movie? (y/n): ")

# Processing & Output
if age < 0 or age > 120:
    print("Error: age must be 0 to 120.")
else:
    if age < 13:
        ticket_type = "Child"
        base_price = CHILD_PRICE
    elif age >= 65:
        ticket_type = "Senior"
        base_price = SENIOR_PRICE
    else:
        ticket_type = "Adult"
        base_price = ADULT_PRICE

    total = base_price
    is_tuesday = day.lower() == "tuesday"
    is_3d = three_d.lower() == "y"

    if is_tuesday:
        total -= TUESDAY_DISCOUNT

    if is_3d:
        total += THREE_D_CHARGE

    print()
    print(f"--- Ticket for {name} ---")
    print(f"Ticket type:   {ticket_type}")
    print(f"Base price:    ${base_price:.2f}")
    if is_tuesday:
        print(f"Tuesday deal: -${TUESDAY_DISCOUNT:.2f}")
    if is_3d:
        print(f"3D charge:     ${THREE_D_CHARGE:.2f}")
    print(f"Total:         ${total:.2f}")






# Author: Student
# Description: Calculates shipping cost and delivery days for an online order.

ZONE1_RATE = 0.50
ZONE2_RATE = 0.75
ZONE3_RATE = 1.25
MINIMUM_SHIPPING = 4.00
FREE_SHIPPING_AMOUNT = 50.00
RUSH_FEE = 10.00

order_total = float(input("Order total: "))
weight = float(input("Package weight (lbs): "))
zone = int(input("Shipping zone (1-3): "))
rush = input("Rush delivery? (y/n): ")


if order_total <= 0 or weight <= 0:
    print("Error: order total and weight must be more than 0.")
elif zone != 1 and zone != 2 and zone != 3:
    print("Error: zone must be 1, 2, or 3.")
else:
    if zone == 1:
        rate = ZONE1_RATE
        days = 2
    elif zone == 2:
        rate = ZONE2_RATE
        days = 4
    else:
        rate = ZONE3_RATE
        days = 6

    shipping = weight * rate

    if shipping < MINIMUM_SHIPPING:
        shipping = MINIMUM_SHIPPING

    is_rush = rush.lower() == "y"

    if order_total >= FREE_SHIPPING_AMOUNT and not is_rush:
        shipping = 0.00

    if is_rush:
        shipping += RUSH_FEE
        if zone == 1 or zone == 2:
            days = 1
        else:
            days = 2

    is_heavy = weight > 50
    if is_heavy:
        days += 2

    grand_total = order_total + shipping

    print()
    print("--- Shipping Summary ---")
    print(f"Order total:  ${order_total:.2f}")
    if shipping == 0:
        print("Shipping:     FREE")
    else:
        print(f"Shipping:     ${shipping:.2f}")
    print(f"Grand total:  ${grand_total:.2f}")

    if days == 1:
        print("Arrives in:   1 day")
    else:
        print(f"Arrives in:   {days} days")

    if is_heavy:
        print("Note: heavy package, 2 extra days added.")





# Program: BPA Eligibility Checker
# Author: Student
# Description: Checks member competition eligibility, event limits, and leadership qualifications.

MIN_GPA = 2.0
OFFICER_GPA = 3.0
HONOR_GPA = 3.5
MAX_EVENTS = 2

# Input
name = input("Member name: ")
grade = int(input("Grade (9-12): "))
gpa = float(input("GPA (0.0-4.0): "))
dues = input("Dues paid? (y/n): ")
events = int(input("Events signed up for: "))

# Processing & Output
if grade < 9 or grade > 12:
    print("Error: grade must be 9 to 12.")
elif gpa < 0.0 or gpa > 4.0:
    print("Error: GPA must be 0.0 to 4.0.")
else:
    dues_paid = dues.lower() == "y"
    is_eligible = dues_paid and gpa >= MIN_GPA

    print()
    print(f"--- BPA Check for {name} ---")

    if is_eligible:
        print("Status: ELIGIBLE")
        if events == 0:
            print("Sign up for at least one event.")
        elif events == 1:
            print("You are entered in 1 event.")
        elif events == MAX_EVENTS:
            print(f"You are entered in {MAX_EVENTS} events.")
        else:
            extra = events - MAX_EVENTS
            print(f"You can only enter {MAX_EVENTS} events. Drop {extra}.")
    else:
        print("Status: NOT ELIGIBLE")
        if not dues_paid:
            print("Reason: dues not paid.")
        if gpa < MIN_GPA:
            print(f"Reason: GPA is below {MIN_GPA}.")

    if (grade == 11 or grade == 12) and gpa >= OFFICER_GPA:
        print("You can run for chapter office.")

    if grade == 12 and gpa >= HONOR_GPA:
        print("Senior honor cord: yes")


