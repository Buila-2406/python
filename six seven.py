print("\n--- Factorial of a Number ---")
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    print("Factorial of", n, "is", fact)
print("\n--- Filter Odd and Even Numbers ---")
raw = input("Enter numbers separated by spaces: ")

nums = list(map(int, raw.split()))

evens = []
odds = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("Even Numbers:", evens)
print("Odd Numbers:", odds)