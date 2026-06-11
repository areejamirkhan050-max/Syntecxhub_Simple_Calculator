# ============================================
#   Simple Calculator - Syntecxhub Internship
#   Project 1 - Python Programming Week 1
# ============================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None  # Divide by zero error
    return a / b

def get_numbers():
    """Parse and validate two numbers from user input."""
    while True:
        try:
            a = float(input("  Enter first number  : "))
            b = float(input("  Enter second number : "))
            return a, b
        except ValueError:
            print("  ❌ Invalid input! Please enter numeric values.\n")

def get_operator():
    """Get a valid operator from user."""
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("  Enter operator (+, -, *, /) : ").strip()
        if op in valid_ops:
            return op
        else:
            print("  ❌ Invalid operator! Choose from +, -, *, /\n")

def calculate(a, op, b):
    """Perform calculation based on operator."""
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)

def show_menu():
    print("\n" + "="*40)
    print("       🧮  SIMPLE CALCULATOR")
    print("="*40)
    print("  [1] Perform a Calculation")
    print("  [2] Clear / New Calculation")
    print("  [3] Exit")
    print("="*40)

def main():
    print("\n  Welcome to Simple Calculator!")
    print("  Syntecxhub Internship - Project 1\n")

    history = []

    while True:
        show_menu()
        choice = input("  Choose an option (1/2/3): ").strip()

        if choice == '1':
            print("\n--- New Calculation ---")
            a, b = get_numbers()
            op = get_operator()
            result = calculate(a, op, b)

            if result is None:
                print("\n  ❌ Error: Cannot divide by zero!")
            else:
                # Format nicely: remove .0 for whole numbers
                a_str = int(a) if a == int(a) else a
                b_str = int(b) if b == int(b) else b
                res_str = int(result) if result == int(result) else round(result, 6)
                print(f"\n  ✅ Result: {a_str} {op} {b_str} = {res_str}")
                history.append(f"{a_str} {op} {b_str} = {res_str}")

            if history:
                print("\n  📋 Calculation History:")
                for i, entry in enumerate(history, 1):
                    print(f"     {i}. {entry}")

        elif choice == '2':
            history.clear()
            print("\n  🔄 History cleared! Ready for new calculations.")

        elif choice == '3':
            print("\n  👋 Thank you for using Simple Calculator!")
            print("  Syntecxhub - Create | Think | Solve\n")
            break

        else:
            print("\n  ❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
