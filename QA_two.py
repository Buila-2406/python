import matplotlib.pyplot as plt

# -------------------------------
# 1. Input Handling
# -------------------------------
patients = {}

for i in range(1, 8):  # Collect 7 patients
    pid = f"P00{i}"
    name = input(f"Enter name for patient {pid}: ").strip().title()
    age = int(input("Enter age: "))
    bp = input("Enter BP (format: systolic/diastolic): ").strip()
    temp = float(input("Enter temperature (°C): "))

    patients[pid] = {"name": name, "age": age, "bp": bp, "temp": temp}

# -------------------------------
# 2. User-Defined Function
# -------------------------------
def analyze_patient(bp_str, temp, age, risk_limit=38.0):
    systolic, diastolic = map(int, bp_str.split("/"))
    fever_flag = temp >= risk_limit
    bp_flag = systolic >= 140 or diastolic >= 90
    senior_flag = age >= 60
    return (systolic, diastolic, fever_flag, bp_flag, senior_flag)

# -------------------------------
# 3. Loop + Conditionals
# -------------------------------
systolic_list = []
temp_list = []
alerts = []

for pid, details in patients.items():
    sys, dia, fever, bp_high, senior = analyze_patient(details["bp"], details["temp"], details["age"])
    systolic_list.append(sys)
    temp_list.append(details["temp"])

    if bp_high:
        alerts.append(f"{details['name']} ({pid}): High BP warning")
    if fever:
        alerts.append(f"{details['name']} ({pid}): Fever alert")
    if senior:
        alerts.append(f"{details['name']} ({pid}): Senior patient note")

# -------------------------------
# 4. Built-in Functions
# -------------------------------
avg_age = round(sum([p["age"] for p in patients.values()]) / len(patients), 1)
avg_sys = round(sum(systolic_list) / len(systolic_list), 1)
max_sys = max(systolic_list)
min_sys = min(systolic_list)

# -------------------------------
# 5. Visualization
# -------------------------------
plt.bar(patients.keys(), systolic_list, color="skyblue")
plt.title("Systolic BP of Patients")
plt.xlabel("Patient ID")
plt.ylabel("Systolic BP")
plt.show()

# -------------------------------
# 6. Output Summary
# -------------------------------
print("\n--- Patient Registry Summary ---")
print(f"Average Age: {avg_age}")
print(f"Average Systolic BP: {avg_sys}")
print(f"Highest Systolic BP: {max_sys}")
print(f"Lowest Systolic BP: {min_sys}")
print(f"Total Fever Cases: {sum([1 for t in temp_list if t >= 38])}")
print(f"Total High BP Cases: {sum([1 for s in systolic_list if s >= 140])}")
print("\nAlerts:")
for a in alerts:
    print("-", a)




