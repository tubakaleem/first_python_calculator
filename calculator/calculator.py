import numpy as np

while True:
    try:
        values = input("Enter values with spaces: ")
        numbers = [float(i) for i in values.split()]
        break   
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

print("\nChoose operation:")
print("1. Sum")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Sine")
print("6. Cosine")
print("7. Tangent")

choice = input("Enter choice (1/2/3/4/5/6/7): ")

if choice == "1":
    result = sum(numbers)
    print("Sum is:", result)

elif choice == "2":
    result = numbers[0] - sum(numbers[1:])
    print("Difference is:", result)

elif choice == "3":
    result = numbers[0]
    for n in numbers[1:]:
        result *= n
    print("Multiplication is:", result)

elif choice == "4":
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            print("Cannot divide by zero 🚫")
            break
        result /= n
    else:
        print("Division is:", result)

elif choice == "5":
    if len(numbers) == 1:
        result = np.sin(np.radians(numbers[0]))
        print("Sine is:", result)
    else:
        print("Please enter only one value.")

elif choice == "6":
    if len(numbers) == 1:
        result = np.cos(np.radians(numbers[0]))
        print("Cosine is:", result)
    else:
        print("Please enter only one value.")

elif choice == "7":
    if len(numbers) == 1:
        result = np.tan(np.radians(numbers[0]))
        print("Tangent is:", result)
    else:
        print("Please enter only one value.")

else:
    print("Invalid choice — the universe does not recognize this operation.")
