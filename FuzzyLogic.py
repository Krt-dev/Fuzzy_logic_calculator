def membership_value(x, membership_set):
    if membership_set == 'a':
        a1_values = {
            0: 10,
            1: 10,
            2: 10,
            3: 10,
            4: 6,
            5: 0
        }

        a2_values = {
            2: 0,
            3: 1,
            4: 3,
            5: 7,
            6: 10,
            7: 7,
            8: 0
        }

        a3_values = {
            4: 0,
            5: 1,
            6: 3,
            7: 6,
            8: 8,
            9: 10,
            10: 10
        }

        # Checking membership for a1
        a1_val = a1_values.get(x, 0)

        # Checking membership for a2
        a2_val = a2_values.get(x, 0)

        # Checking membership for a3
        a3_val = a3_values.get(x, 0)

        return a1_val, a2_val, a3_val

    elif membership_set == 'b':
        b1_values = {
            0: 10,
            1: 10,
            2: 10,
            3: 10,
            4: 7,
            5: 5,
            6: 3,
            7: 0
        }

        b2_values = {
            3: 0,
            4: 1,
            5: 4,
            6: 5,
            7: 8,
            8: 10,
            9: 10,
            10: 10
        }

        # Checking membership for b1
        b1_val = b1_values.get(x, 0)

        # Checking membership for b2
        b2_val = b2_values.get(x, 0)

        return b1_val, b2_val


input_x_a = int(input("Enter a value for X (between 0 and 10) for 'a': "))
input_x_b = int(input("Enter a value for X (between 0 and 10) for 'b': "))

# Calling the function separately for 'a' and 'b' memberships
a1, a2, a3 = membership_value(input_x_a, 'a')
b1, b2 = membership_value(input_x_b, 'b')

# Printing the individually assigned variables
print("The values of a's are as follows")
print(f"a1: {a1}")
print(f"a2: {a2}")
print(f"a3: {a3}")

print("The vales of b's are as of follows")
print(f"b1: {b1}")
print(f"b2: {b2}")


# Comparing values and assigning to c1, c2, c3
c1 = max(a3, b1)
c2 = min(a2, b2)
c3 = a1

# Printing the assigned variables
print("The values of c are as of follows")
print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c3: {c3}")

# Initialize canswersC1, canswersC2, and canswersC3 with their initial values
canswersC1 = {0: 10, 1: 10, 2: 10, 3: 10, 4: 7, 5: 5, 6: 0}
canswersC2 = {2: 0, 3: 4, 4: 8, 5: 10, 6: 5, 7: 0}
canswersC3 = {4: 0, 5: 4, 6: 7, 7: 9, 8: 0, 9: 0, 10: 0}

# Update canswersC1 values based on c1
max_c1 = max(c1, max(canswersC1.values()))
for x in canswersC1:
    if canswersC1[x] > c1:
        canswersC1[x] = c1

# Update canswersC2 values based on c2
max_c2 = max(c2, max(canswersC2.values()))
for x in canswersC2:
    if canswersC2[x] > c2:
        canswersC2[x] = c2

# Update canswersC3 values based on c3
max_c3 = max(c3, max(canswersC3.values()))
for x in canswersC3:
    if canswersC3[x] > c3:
        canswersC3[x] = c3

# Handling overlaps between canswersC1 and canswersC2
overlap_1_2 = set(canswersC1.keys()).intersection(canswersC2.keys())
if overlap_1_2:
    max_overlap_1_2 = max(max(canswersC1[x], canswersC2[x]) for x in overlap_1_2)
    for x in overlap_1_2:
        canswersC1[x] = max_overlap_1_2
        canswersC2[x] = max_overlap_1_2

# Handling overlaps between canswersC1 and canswersC3
overlap_1_3 = set(canswersC1.keys()).intersection(canswersC3.keys())
if overlap_1_3:
    max_overlap_1_3 = max(max(canswersC1[x], canswersC3[x]) for x in overlap_1_3)
    for x in overlap_1_3:
        canswersC1[x] = max_overlap_1_3
        canswersC3[x] = max_overlap_1_3

# Handling overlaps between canswersC2 and canswersC3
overlap_2_3 = set(canswersC2.keys()).intersection(canswersC3.keys())
if overlap_2_3:
    max_overlap_2_3 = max(max(canswersC2[x], canswersC3[x]) for x in overlap_2_3)
    for x in overlap_2_3:
        canswersC2[x] = max_overlap_2_3
        canswersC3[x] = max_overlap_2_3

# Displaying the max values of 1-10 individually
max_values = {
    x: max(canswersC1.get(x, 0), canswersC2.get(x, 0), canswersC3.get(x, 0))
    for x in range(1, 11)
}
print("Max values of 1-10:")
for x in range(1, 11):
    print(f"Max value of {x}: {max_values[x]}")


# Calculate numerator and denominator for the specified formula
numerator = sum(x * max(canswersC1.get(x, 0), canswersC2.get(x, 0), canswersC3.get(x, 0)) for x in range(1, 11))
denominator = sum(max(canswersC1.get(x, 0), canswersC2.get(x, 0), canswersC3.get(x, 0)) for x in range(1, 11))

# Avoid division by zero
if denominator != 0:
    result = (numerator / denominator) * 10
else:
    result = 0  # Define a default value if denominator is zero

# Format the result to two decimal places and multiply by 100
formatted_result = "{:.2f}".format(result)

print(f"Result: {formatted_result}%")