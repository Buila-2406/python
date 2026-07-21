# PROGRAM 8: Sum of numbers in a list
def sum_of_list():
    print("\n=== SUM OF ELEMENTS IN A LIST ===")

    raw = (input("Enter numbers separated by spaces: "))
    numbers = list(map(int, raw.split()))

    # Sum using loop
    total_loop = 0
    for num in numbers:
        total_loop += num

    # Sum using built-in function
    total_builtin = sum(numbers)

    print("Numbers:", numbers)
    print("Sum (using loop):", total_loop)
    print("Sum (using sum()):", total_builtin)


# PROGRAM 10: Fibonacci sequence up to n terms
def fibonacci():
    print("\n=== FIBONACCI SEQUENCE ===")

    n = int(input("Enter the number of terms: "))

    if n <= 0:
        print("Please enter a positive number.")
        return

    a, b = 0, 1  # two variables can be assigned like this in python

    if n == 1:
        print(a)
        return

    print("Fibonacci sequence:")
    print(a, b, end=" ")

    for _ in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()  # New line
"""
| a | b | c = a+b |
| - | - | ------- |
| 0 | 1 | 1       |
| 1 | 1 | 2       |
| 1 | 2 | 3       |
| 2 | 3 | 5       |
"""



# --------------------------------------------------------
# MAIN MENU USING match-case
# --------------------------------------------------------

while True:
    print("\n===================================")
    print("      PYTHON MENU (match-case)      ")
    print("===================================")
    print("1. Sum of Elements in a List")
    print("2. Fibonacci Sequence")
    print("3. Exit")
    print("===================================")

    choice = input("Enter your choice (1-3): ")

    match choice:
        case "1":
            sum_of_list()
        case "2":
            fibonacci()
        case "3":
            print("Exiting Program. Goodbye!")
            break
        case _:
            print("Invalid choice! Please select 1, 2, or 3.")
