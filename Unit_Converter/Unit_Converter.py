def length_converter():
    print("1. Meters to Kilometers")
    print("2. Kilometers to Miles")
    choice = input("Choose conversion: ")
    value = float(input("Enter value: "))

    if choice == '1':
        print(f"{value} meters = {value / 1000} kilometers")
    elif choice == '2':
        print(f"{value} kilometers = {value * 0.621371} miles")

def temperature_converter():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Kelvin")
    choice = input("Choose conversion: ")
    value = float(input("Enter value: "))

    if choice == '1':
        print(f"{value}°C = {(value * 9/5) + 32}°F")
    elif choice == '2':
        print(f"{value}°F = {((value - 32) * 5/9) + 273.15}K")

def main():
    print("==== Unit Converter ====")
    print("1. Length")
    print("2. Temperature")
    choice = input("Choose type: ")

    if choice == '1':
        length_converter()
    elif choice == '2':
        temperature_converter()
    else:
        print("Invalid choice")

main()
