import os

def clear_screen():
    """Clear the terminal screen on Windows and Unix-like systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    """Display the menu options and return the user's choice."""
    print("\nSimple Calculator")
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("0. Exit")
    choice = input("\nEnter choice (1/2/3/4/5/0): ")
    return choice

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def exponentiate(x, y): return x ** y

# Map each menu option to its label, operator symbol, and implementation.
operations = {
    '1': ("Add", "+", add),
    '2': ("Subtract", "-", subtract),
    '3': ("Multiply", "*", multiply),
    '4': ("Divide", "/", divide),
    '5': ("Exponentiate", "**", exponentiate),
}

def main():
    """Run the interactive calculator until the user chooses to exit."""
    while True:
        clear_screen()
        choice = menu()

        if choice in operations:
            name, symbol, func = operations[choice]
            print(f"\n{name} Selected")
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            result = func(num1, num2)
            print(f"\n{num1} {symbol} {num2} = {result}")
            input("\nPress Enter to continue...")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid input.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
