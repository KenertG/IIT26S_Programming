print("Program starting.")
print(f"Insert two integers.")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))
print(f"Comparing inserted integers {int1} and {int2}.")
if int1 == int2:
    print("Integers are the same")
elif int1 > int2:
    print("First integer is greater")
else:
    print("Second integer is greater")
print()
print(f"Adding integers together")
print(f"{int1} + {int2} = {int1 + int2}")
print()
print("Checking the parity of the sum")
total = int1 + int2
if total % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")
print("Program ending.")
