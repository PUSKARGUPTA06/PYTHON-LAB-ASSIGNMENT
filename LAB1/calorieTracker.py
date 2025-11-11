import datetime
print("Welcome to Daily Calorie Tracker")
print("This tool helps you log meals, track total calorie intake, compare it with your daily limit, and optionally save your session.\n")
meal_names = []
meal_calories = []
num_meals = int(input("How many meals do you want to enter today? : "))
for i in range(num_meals):
    meal = input(f"Enter meal #{i+1} name: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    meal_calories.append(cal)
total_calories = sum(meal_calories)
average_calories = total_calories / len(meal_calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))
if total_calories > daily_limit:
    status = "You are not in your daily calorie limit!"
else:
    status = "You are in your daily calorie limit!"
print("YOUR DAILY CALORIE's")
print("Meal Name\tCalories")

for meal, cal in zip(meal_names, meal_calories):
    print(f"{meal}\t\t{cal}")

print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")

print(status)
save = input("\nDo you want to save this session report? (yes/no): ").lower()
if save == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calorie_log.txt", "w") as file:
        file.write("===== Daily Calorie Tracker Report =====\n")
        file.write(f"Date & Time: {timestamp}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("--------------------------------\n")
        for meal, cal in zip(meal_names, meal_calories):
            file.write(f"{meal}\t\t{cal}\n")
        file.write("--------------------------------\n")
        file.write(f"Total:\t\t{total_calories}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write("--------------------------------\n")
        file.write(f"Status: {status}\n")

    print(" Session saved successfully in 'calorie_log.txt'!")

print("\nThank you for using Daily Calorie Tracker! Stay fit ")
