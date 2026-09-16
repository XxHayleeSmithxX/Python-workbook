# Task: String Formatting
# Objective 3.2 - Construct and analyze code segments that perform console I/O
#
# Instructions:
# Using the variables below, format strings using .format() and f-strings.
#
# Expected output:
# line_1: Alice is 17 years old.
# line_2: Price: $9.99
# line_3: Alice is 17 years old.
# line_4: Price: $9.99

name = "Alice"
age = 17
price = 9.99

# Step 1: Use .format() — "[name] is [age] years old."
line_1 = ("{0} is {1} years old.".format(name, age, price))
print("line_1:", line_1)

# Step 2: Use .format() — "Price: $[price]" (2 decimal places)
line_2 = ("Price: ${2}".format(name, age, price))
print("line_2:", line_2)

# Step 3: Use an f-string — "[name] is [age] years old."
line_3 = (f"{name} is {age} years old.")
print("line_3:", line_3)

# Step 4: Use an f-string — "Price: $[price]" (2 decimal places)
line_4 = (f"Price: ${price}")
print("line_4:", line_4)
