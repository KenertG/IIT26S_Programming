print("Program starting.")
print()
word = input("Insert a closed compound word: ")

print(f"The word you inserted is '{word}' and in reverse it is '{word[::-1]}'.")
print(f"The inserted word length is {len(word)}")
print(f"Last character is '{word[-1]}'")

print()
print("Take substring from the inserted word by inserting...")
start = int(input("Starting point: "))
End = int(input("Ending point: "))
Step = int(input("Step size: "))

substring = word[start:End:Step]

print()
print(f"The word '{word}' sliced to the defined substring is '{substring}'.")

print("Program ending.")