# ==========================================
# Project: Logic Box
# Pattern Generator and Number Analyzer
# ==========================================

def generate_pattern():
    """Generate a right-angled triangle pattern."""

    while True:
        try:
            rows = int(input("\nEnter the number of rows: "))

            if rows <= 0:
                print("Invalid row count! Rows must be greater than 0.")
                break      # Using break

            print("\nRight-Angled Triangle:\n")

            # Nested loops
            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end=" ")
                print()

            print("\nPattern Generated Successfully!")
            break

        except ValueError:
            print("Please enter a valid integer.")


def analyze_numbers():
    """Analyze numbers in a given range."""

    while True:
        try:
            start = int(input("\nEnter the start number: "))
            end = int(input("Enter the end number: "))

            if end < start:
                print("End number must be greater than or equal to start number.")
                continue      # Using continue

            total = 0

            print("\n========== Number Analysis ==========\n")

            for number in range(start, end + 1):

                # Example of pass statement
                if number == 0:
                    pass

                if number % 2 == 0:
                    print(f"Number {number} is Even")
                else:
                    print(f"Number {number} is Odd")

                total += number

            print("\n-------------------------------------")
            print(f"Sum of all numbers from {start} to {end} is: {total}")
            print("-------------------------------------")
            print("Analysis Completed Successfully!")

            break

        except ValueError:
            print("Invalid input! Please enter integers only.")


def show_menu():
    """Display Menu"""

    print("\n=======================================")
    print(" Pattern Generator & Number Analyzer")
    print("=======================================")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")


def thank_you():
    """Display Final Closing Message"""

    print("\n========================================================")
    print("        THANK YOU FOR USING OUR PROJECT")
    print("========================================================")
    print("      Pattern Generator & Number Analyzer")
    print("--------------------------------------------------------")
    print("This program demonstrated the use of:")
    print("-> Functions")
    print("-> Nested Loops")
    print("-> Conditional Statements")
    print("-> break, continue and pass")
    print("-> Exception Handling")
    print("--------------------------------------------------------")
    print("Project Completed Successfully!")
    print("Keep Learning, Keep Coding!")
    print("Have a Wonderful Day!")
    print("========================================================")


def main():

    print("========================================================")
    print(" Welcome to the Pattern Generator and Number Analyzer!")
    print("========================================================")
    print("This program can:")
    print("1. Generate a Right-Angled Triangle Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Check Odd and Even Numbers")
    print("4. Calculate the Sum of Numbers")
    print("========================================================")

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            generate_pattern()

        elif choice == "2":
            analyze_numbers()

        elif choice == "3":
            thank_you()
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()
