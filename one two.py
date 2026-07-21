def arithmetic_operations():
    print("\n--- Arithmetic Operations ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Choose Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (A,S,M,D): ")

    if choice == "a" or choice == "A":
        print("Result:", a + b)
    elif choice == "s" or choice == "S":
        print("Result:", a - b)
    elif choice == "m" or choice == "M":
        print("Result:", a * b)
    elif choice == "d" or choice =="D":
        if b != 0:
            print("Result:", f"{a/b:.3f}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice!")

arithmetic_operations()
print("\n--- Check Positive / Negative / Zero ---")
n = float(input("Enter a number: "))

if n > 0:
    print("The number is Positive.")
elif n < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")