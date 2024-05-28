"""
Author: Daniel Yazgi
Date: 2024-05-28
"""
def greet(name):
    """Function to greet a person by name."""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"

class Greeter:
    """Class to handle greeting operations."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        """Method to return a greeting message."""
        return greet(self.name)

def main():
    """Main function to run the script."""
    try:
        # Create a Greeter object
        greeter = Greeter("World")
        # Print the greeting message
        print(greeter.greet())
    except ValueError as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    # this is a minor change
    main()
