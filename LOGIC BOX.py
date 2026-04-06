p1rint("🦚JAY SHREE KRISHNA🦚")

def generate_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)

def analyze_range(start, end):
    total = 0
    for num in range(start, end + 1):
        print(f"Number {num} is {'Even' if num % 2 == 0 else 'Odd'}")
        total += num
    print(f"Sum of all numbers from {start} to {end} is: {total}")

def main():
    print("Welcome to the Pattern Generator and Number Analyzer!\n")
    while True:
        print("Select an option:")
        print("1. Generate a Pattern")
        print("2. Analyze a Range of Numbers")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            rows = int(input("Enter the number of rows for the pattern: "))
            generate_pattern(rows)
        elif choice == '2':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            analyze_range(start, end)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()