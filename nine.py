# ------------------------------------------------------------
# PROGRAM: Demonstration of Exception Handling in Python
# ------------------------------------------------------------

print("=== PYTHON EXCEPTION HANDLING DEMO ===")

try:
    # Asking for user input (may cause ValueError)
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    # Performing division (may cause ZeroDivisionError)
    result = num1 / num2

# ------------------------------------------------------------
# EXCEPTION BLOCKS
# ------------------------------------------------------------

# Handles case where user enters non-numeric input
except ValueError:
    print("\nError: Please enter ONLY numbers.")
    print("Example of valid input: 10  or  25")

# Handles case where denominator is zero
except ZeroDivisionError:
    print("\nError: Division by ZERO is not allowed.")
    print("Please provide a non-zero denominator.")

# Catches any unexpected error
except Exception as e:
    print("\nAn unexpected error occurred:", e)

# ------------------------------------------------------------
# ELSE BLOCK (runs only when NO exception occurs)
# ------------------------------------------------------------
else:
    print("\nNo errors occurred.")
    print("Division Result:", result)

# ------------------------------------------------------------
# FINALLY BLOCK (always runs)
# ------------------------------------------------------------
finally:
    print("\nExecution Completed. (This message always appears)")
    print("Thank you for using the program.")
