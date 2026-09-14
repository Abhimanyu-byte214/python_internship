import math

print("================================")
print("        NUMBER CHECKER")
print("================================")

values = []

total_numbers = int(input("How many numbers do you want to enter? "))

for i in range(total_numbers):
    value = float(input("Enter number " + str(i + 1) + ": "))
    values.append(value)


def check_prime(value):

    if value < 2:
        return False

    if value != int(value):
        return False

    value = int(value)

    for number in range(2, int(math.sqrt(value)) + 1):

        if value % number == 0:
            return False

    return True


print("\n========== NUMBER DETAILS ==========")

for value in values:

    print("\nNumber:", value)

    # Check positive, negative or zero
    if value > 0:
        print("Positive number")

    elif value < 0:
        print("Negative number")

    else:
        print("Zero")

    # Check even or odd
    if value == int(value):

        if int(value) % 2 == 0:
            print("Even number")

        else:
            print("Odd number")

    else:
        print("Not a whole number")

    # Check prime
    if check_prime(value):
        print("Prime number: Yes")

    else:
        print("Prime number: No")


if len(values) > 0:

    total = sum(values)
    average = total / len(values)

    print("\n========== FINAL RESULT ==========")

    print("Total numbers:", len(values))
    print("Total:", total)
    print("Average:", average)
    print("Highest:", max(values))
    print("Lowest:", min(values))

else:
    print("\nNo numbers were entered.")

print("\nThank you for using the Number Checker!")
