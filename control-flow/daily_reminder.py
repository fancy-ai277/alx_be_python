# daily_reminder.py

# Step 1: Ask the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Use match case for priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority"

# Step 3: Modify message if time-bound
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Step 4: Print the reminder
print("Reminder:", message)

