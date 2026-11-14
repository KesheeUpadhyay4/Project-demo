import os

# Create history file in the same folder as this Python file
HISTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "history.txt")


# Function to show calculation history
def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No history found!")
        else:
            print("\n--- Calculation History ---")
            for line in reversed(lines):
                print(line.strip())

    except FileNotFoundError:
        print("No history found!")


# Function to clear history
def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        file.close()

    print("History cleared.")


# Function to save calculation history
def save_to_history(user_input, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{user_input} = {result}\n")


# Calculator function
def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input. Use format: number operator number (e.g. 8 + 8)")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])

        if op == "+":
            result = num1 + num2

        elif op == "-":
            result = num1 - num2

        elif op == "*":
            result = num1 * num2

        elif op == "/":
            if num2 == 0:
                print("Cannot divide by zero")
                return
            result = num1 / num2

        else:
            print("Invalid operator. Use only +, -, *, /")
            return

        if result.is_integer():
            result = int(result)

        print("Result:", result)

        save_to_history(user_input, result)

    except ValueError:
        print("Please enter valid numbers.")


# Main function
def main():
    print("--- SIMPLE CALCULATOR (type history, clear or exit) ---")

    while True:
        user_input = input(
            "Enter calculation (+ - * /) or command (history, clear, exit): "
        ).strip()

        if user_input == 'exit':
            print("Goodbye!")
            break

        elif user_input == 'history':
            show_history()

        elif user_input == 'clear':
            clear_history()

        else:
            calculate(user_input)


# Start the calculator
if __name__ == "__main__":
    main()