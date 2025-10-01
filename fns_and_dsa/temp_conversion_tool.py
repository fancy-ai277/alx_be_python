# temp_conversion_tool.py

# ---- Global Conversion Factors ----
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9   # used for (F - 32) * (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5   # used for (C * (9/5)) + 32
FAHRENHEIT_OFFSET = 32                 # offset between Celsius and Fahrenheit scales


# ---- Conversion Functions ----
def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global FAHRENHEIT_TO_CELSIUS_FACTOR
    Formula: C = (F - 32) * (5/9)
    """
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global CELSIUS_TO_FAHRENHEIT_FACTOR
    Formula: F = (C * (9/5)) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET


# ---- User Interaction ----
if __name__ == "__main__":
    try:
        # Prompt user for temperature input
        temp_input = input("Enter the temperature to convert: ")

        # Validate numeric input
        if not temp_input.replace(".", "", 1).lstrip("-").isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_input)

        # Prompt user for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")

        elif unit == "C":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")

        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)
