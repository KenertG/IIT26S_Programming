print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print()
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = input("Your choice: ")
print()

if choice == "1":
    print("Length options:")
    print("1 - Meters to Kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice2 = input("Your choice: ")
    if choice2 == "1":
        m = float(input("Insert meters: "))
        kilometers = m / 1000
        print(f"{m} m is {kilometers} km")
    elif choice2 == "2":
        km = float(input("Insert kilometers: "))
        m = km * 1000
        print(f"{km} km is {m} m")
    elif choice2 == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == "2":
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice3 = input("Your choice: ")
    if choice3 == "1":
        g = float(input("Insert grams: "))
        pounds = g / 453.592
        print(f"{g} g is {pounds:.2f} lb")
    elif choice3 == "2":
        lb = float(input("Insert pounds: "))
        grams = lb * 453.592
        print(f"{lb} lb is {grams:.2f} g")
    elif choice3 == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == "0":
    print("Exiting...")

else:
    print("Unknown option.")

print()
print("Program ending.")