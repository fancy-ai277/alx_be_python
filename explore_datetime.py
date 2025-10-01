from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    # Show current date and time
    display_current_datetime()

    # Ask user for number of days
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days = int(days_input)  # validate input as integer
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer value for days.")
