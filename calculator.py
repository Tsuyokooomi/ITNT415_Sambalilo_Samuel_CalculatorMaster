import os

os.system("")  # design: enables colors in the Windows terminal

# design: colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

def add(x, y):
    return round(x+y,6)

def subtract(x, y):
    return round(x-y,6)

def multiply(x, y):
    return round(x*y,6)

def divide(x, y):
    if y == 0:
        print(f"{RED}Error: Cannot divide by zero.{RESET}")
        return None
    return round(x/y,6)

def get_number(prompt):
    while True:
        try:
            return float(input(f"{CYAN}> {prompt}{RESET}"))
        except ValueError:
            print(f"{RED}Invalid number. Try again.{RESET}")

def main():
    while True:
        print(f"\n{CYAN}╔══════════════════════════════╗{RESET}")
        print(f"{CYAN}║{RESET}{BOLD}{YELLOW}       CALCULATOR MASTER      {RESET}{CYAN}║{RESET}")
        print(f"{CYAN}╠══════════════════════════════╣{RESET}")
        print(f"{CYAN}║{RESET} {GREEN}{'1. Addition'.ljust(29)}{RESET}{CYAN}║{RESET}")
        print(f"{CYAN}║{RESET} {GREEN}{'2. Subtraction'.ljust(29)}{RESET}{CYAN}║{RESET}")
        print(f"{CYAN}║{RESET} {GREEN}{'3. Multiplication'.ljust(29)}{RESET}{CYAN}║{RESET}")
        print(f"{CYAN}║{RESET} {GREEN}{'4. Division'.ljust(29)}{RESET}{CYAN}║{RESET}")
        print(f"{CYAN}║{RESET} {RED}{'5. Exit'.ljust(29)}{RESET}{CYAN}║{RESET}")
        print(f"{CYAN}╚══════════════════════════════╝{RESET}")

        choice = input(f"{CYAN}Choose an option (1-5): {RESET}")

        if choice == "1":
            x = get_number("Enter first number: ")
            y = get_number("Enter second number: ")
            print(f"{GREEN}{BOLD}Result: {add(x, y)}{RESET}")

        if choice == "2":
            x = get_number("Enter first number: ")
            y = get_number("Enter second number: ")
            print(f"{GREEN}{BOLD}Result: {subtract(x, y)}{RESET}")

        if choice == "3":
            x = get_number("Enter first number: ")
            y = get_number("Enter second number: ")
            print(f"{GREEN}{BOLD}Result: {multiply(x, y)}{RESET}")

        if choice == "4":
            x = get_number("Enter first number: ")
            y = get_number("Enter second number: ")
            result = divide(x, y)
            if result is not None:
                print(f"{GREEN}{BOLD}Result: {result}{RESET}")

        if choice == "5":
            print(f"{GREEN}Goodbye!{RESET}")
            break

        if choice not in ("1", "2", "3", "4"):
            print(f"{RED}Invalid choice. Try again.{RESET}")
            continue

if __name__ == "__main__":
    main()