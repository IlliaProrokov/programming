# Task A: Pizza Party Planner
# Description: Calculates pizzas, extra slices, total cost, and cost per person.


SLICES_PER_PIZZA = 8
PIZZA_PRICE = 12.99
SLICE_PRICE = 2.25


host_name = input("Host name: ")
num_people = int(input("Number of people: "))
slices_per_person = int(input("Slices per person: "))


total_slices = num_people * slices_per_person
whole_pizzas = total_slices // SLICES_PER_PIZZA
extra_slices = total_slices % SLICES_PER_PIZZA
total_cost = (whole_pizzas * PIZZA_PRICE) + (extra_slices * SLICE_PRICE)
cost_per_person = total_cost / num_people

print()
print(f"=== Pizza Plan for {host_name}'s Party ===")
print(f"Slices needed:    {total_slices}")
print(f"Whole pizzas:     {whole_pizzas}")
print(f"Extra slices:     {extra_slices}")
print(f"Total cost:       ${total_cost:.2f}")
print(f"Cost per person:  ${cost_per_person:.2f}")





# Task B: Road Trip Calculator
# Description: Calculates fuel, cost breakdown, and drive time for a road trip.


AVERAGE_SPEED = 55


destination = input("Destination: ")
trip_distance = float(input("Trip distance (miles): "))
miles_per_gallon = float(input("Car's miles per gallon: "))
gas_price = float(input("Gas price per gallon: "))
num_people = int(input("Number of people splitting the cost: "))

gallons_needed = trip_distance / miles_per_gallon
total_gas_cost = gallons_needed * gas_price
cost_per_person = total_gas_cost / num_people

total_minutes = int((trip_distance / AVERAGE_SPEED) * 60)
hours = total_minutes // 60
minutes = total_minutes % 60

round_trip_gas = total_gas_cost * 2


print()
print(f"--- Trip to {destination} ---")
print(f"Gallons of gas:   {gallons_needed:.1f}")
print(f"Gas cost:         ${total_gas_cost:.2f}")
print(f"Cost per person:  ${cost_per_person:.2f}")
print(f"Driving time:     {hours} hr {minutes} min (at {AVERAGE_SPEED} mph)")
print(f"Round trip gas:   ${round_trip_gas:.2f}")



# Task C: Paycheck Calculator
# Description: Calculates weekly net pay and tax deductions alongside yearly projections.

# Constants
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52

# Input
employee_name = input("Employee name: ")
hourly_rate = float(input("Hourly pay rate: "))
hours_worked = float(input("Hours worked this week: "))

# Processing: Paycheck & Taxes
gross_pay = hourly_rate * hours_worked
federal_tax = gross_pay * FEDERAL_TAX_RATE
state_tax = gross_pay * STATE_TAX_RATE
social_security_tax = gross_pay * SOCIAL_SECURITY_RATE
medicare_tax = gross_pay * MEDICARE_RATE

total_deductions = federal_tax + state_tax + social_security_tax + medicare_tax
net_pay = gross_pay - total_deductions
percent_kept = (net_pay / gross_pay) * 100

# Processing: Yearly Totals
yearly_gross = gross_pay * WEEKS_PER_YEAR
yearly_net = net_pay * WEEKS_PER_YEAR

# Output
print()
print("=" * 32)
print(f"PAY STUB: {employee_name}")
print("=" * 32)
print(f"Hours worked:      {hours_worked:.1f}")
print(f"Hourly rate:       ${hourly_rate:.2f}")
print(f"Gross pay:         ${gross_pay:.2f}")
print("-" * 32)
print(f"Federal tax (10%): ${federal_tax:.2f}")
print(f"State tax (3.5%):  ${state_tax:.2f}")
print(f"Social Security:   ${social_security_tax:.2f}")
print(f"Medicare:          ${medicare_tax:.2f}")
print(f"Total taken out:   ${total_deductions:.2f}")
print("-" * 32)
print(f"NET PAY:           ${net_pay:.2f}")
print("=" * 32)
print(f"You keep {percent_kept:.1f}% of what you earn.")
print(f"Yearly gross: ${yearly_gross:.2f}")
print(f"Yearly net:   ${yearly_net:.2f}")
