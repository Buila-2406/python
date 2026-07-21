# Student Mark Sheet Processor

# Function to validate marks
def validate_marks(marks):
    # conditionals + built-in function (all)
    return all(0 <= m <= 100 for m in marks)

# Function to calculate grade
def calculate_grade(average):
    # conditionals
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"

# Main program
def process_students():
    students = {}  # dictionary to store results (built-in data type)

    n = int(input("Enter number of students: "))  # input
    for i in range(n):  # loop
        name = input(f"\nEnter name of student {i+1}: ")
        marks = []

        # loop for subjects
        for subject in ["Math", "Science", "English"]:
            m = int(input(f"Enter marks for {subject} (0-100): "))
            marks.append(m)

        # validate marks
        if not validate_marks(marks):
            print("❌ Invalid marks entered. Skipping student.")
            continue

        # built-in functions: sum, len, max, min
        total = sum(marks)
        average = total / len(marks)
        highest = max(marks)
        lowest = min(marks)
        grade = calculate_grade(average)

        # store in dictionary
        students[name] = {
            "Total": total,
            "Average": average,
            "Highest": highest,
            "Lowest": lowest,
            "Grade": grade
        }

    # final output
    print("\n📊 Student Report Card Summary:")
    for name, details in students.items():
        print(f"\n{name}:")
        for key, value in details.items():
            print(f"  {key}: {value}")

# Run the program
process_students()
