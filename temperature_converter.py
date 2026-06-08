def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def display_menu():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")


def get_temperature(unit):
    return float(input(f"Enter temperature in {unit}: "))


def main():
    display_menu()
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        temp = get_temperature("Celsius")
        result = celsius_to_fahrenheit(temp)
        print(f"\n{temp}°C = {result:.2f}°F")

    elif choice == "2":
        temp = get_temperature("Fahrenheit")
        result = fahrenheit_to_celsius(temp)
        print(f"\n{temp}°F = {result:.2f}°C")

    else:
        print("Invalid choice. Please select 1 or 2.")


main()
