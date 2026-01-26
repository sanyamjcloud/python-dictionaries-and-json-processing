import json

# Store student details using dictionary
students = {
    "101": {
        "name": "Sanyam Jain",
        "age": 20,
        "course": "BCA"
    },
    "102": {
        "name": "Amit Kumar",
        "age": 21,
        "course": "BSc"
    }
}

# Access keys and values
print("Keys:", students.keys())
print("Values:", students.values())

# Update entry
students["101"]["age"] = 21

# Delete entry
del students["102"]

# Loop through dictionary
for roll, details in students.items():
    print("\nRoll No:", roll)
    for key, value in details.items():
        print(f"{key}: {value}")

# Convert dictionary to JSON
json_data = json.dumps(students, indent=4)

# Save JSON to file
with open("students.json", "w") as file:
    file.write(json_data)

# Read JSON back into Python
with open("students.json", "r") as file:
    data = json.load(file)

# Print clean formatted output
print("\nFormatted Output:")
for roll, details in data.items():
    print(f"\nRoll No: {roll}")
    print(f"Name   : {details['name']}")
    print(f"Age    : {details['age']}")
    print(f"Course : {details['course']}")
