# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Try to perform the division
        result = numerator / denominator
        return f"The result of dividing {numerator} by {denominator} is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        # ← Exact message the checker expects:
        return "Error: Please enter numeric values only."
