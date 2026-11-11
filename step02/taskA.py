# Task A: Pizza Party Planner
# Description: Calculates pizzas, extra slices, total cost, and cost per person.

# Constants
SLICES_PER_PIZZA = 8
PIZZA_PRICE = 12.99
SLICE_PRICE = 2.25

# Input
host_name = input("Host name: ")
num_people = int(input("Number of people: "))
slices_per_person = int(input("Slices per person: "))

# Processing
total_slices = num_people * slices_per_person
whole_pizzas = total_slices // SLICES_PER_PIZZA
extra_slices = total_slices % SLICES_PER_PIZZA
total_cost = (whole_pizzas * PIZZA_PRICE) + (extra_slices * SLICE_PRICE)
cost_per_person = total_cost / num_people

# Output
print()
print(f"=== Pizza Plan for {host_name}'s Party ===")
print(f"Slices needed:    {total_slices}")
print(f"Whole pizzas:     {whole_pizzas}")
print(f"Extra slices:     {extra_slices}")
print(f"Total cost:       ${total_cost:.2f}")
print(f"Cost per person:  ${cost_per_person:.2f}")
