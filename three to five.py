print("\n--- Odd or Even Check ---")
n = int(input("Enter an integer: "))

if n % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

print("\n--- Leap Year Check ---")
year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")

print("\n--- Prime Number Check ---")
n = int(input("Enter an integer: "))

if n <= 1:
    print(n, "is NOT a prime number.")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "IS a prime number.")
    else:
        print(n, "is NOT a prime number.")