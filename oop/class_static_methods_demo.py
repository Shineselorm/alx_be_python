class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers (does not depend on class/instance)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Return the product of two numbers and show class-level attribute.
        Uses cls to access class attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
