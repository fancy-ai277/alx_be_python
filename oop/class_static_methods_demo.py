class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage (optional, can be tested separately)
if __name__ == "__main__":
    print("Addition:", Calculator.add(5, 3))
    print("Multiplication:", Calculator.multiply(5, 3))
