HISTORY_FILE = 'history.txt'

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
        if len(lines) == 0:
            print("No history available.")
        else:
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print("No history available.")

def clear_history():
    with open(HISTORY_FILE, "w") as file:
        pass
    print("History cleared.")

def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: number operator number")
        return None

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Please enter valid numeric values.")
        return None

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero.")
            return None
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return None

    # Convert to int if result is whole number
    if result.is_integer():
        result = int(result)

    # Save and return
    save_to_history(user_input, result)
    return result

def main():
    print("--- SIMPLE CALCULATOR (type history, clear or exit) ---")
    while True:
        user_input = input("Enter calculation (+, -, *, /) or command 'history', 'clear', 'exit': ").strip().lower()
        if user_input == "exit":
            print("Exiting calculator. Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            result = calculate(user_input)
            if result is not None:
                print(f"Result: {result}")

if __name__ == "__main__":
    main()

