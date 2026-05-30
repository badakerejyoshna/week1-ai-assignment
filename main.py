import json
from datetime import datetime

# Load tips and quotes from JSON file
with open("tips.json", "r") as file:
    data = json.load(file)

name = input("Enter your name: ")

print(f"\nWelcome, {name}!")
print("\nSmart Student Assistant")
print("1. Generate Study Tip")
print("2. Generate Motivation Quote")
print("3. Display Current Date & Time")

choice = input("\nChoose an option (1-3): ")

result = ""

if choice == "1":
    result = data["study_tips"][0]
    print("\nStudy Tip:")
    print(result)

elif choice == "2":
    result = data["motivation_quotes"][0]
    print("\nMotivation Quote:")
    print(result)

elif choice == "3":
    result = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("\nCurrent Date & Time:")
    print(result)

else:
    result = "Invalid choice."
    print(result)

# Save output to file
with open("output.txt", "a") as file:
    file.write(f"\n{name}: {result}")

print("\nOutput saved to output.txt")