# -*- coding: utf-8 -*-
"""Clean Practices.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pAgKPOYrXHZK5nz4DJf0KD5nY7cNSpRi

**File Handling**: The **save_user_data** and **read_user_data** functions handle saving and reading data from a file (user_data.txt). We use with open() to ensure files are properly closed after operations, preventing issues like memory leaks or file locks.

**Descriptive Variable Names**: The variables filename, name, age, user_name, and user_age are all descriptive, clearly showing their role in the code.

**Comments**: Key sections of the code are explained with comments, especially the steps where files are handled and where errors could potentially occur.

**Avoiding Hardcoding**: Instead of hardcoding data, the program uses user input for name and age, making the code dynamic and reusable.
"""

# Function to save user data to a file
def save_user_data(filename, name, age):
    try:
        with open(filename, 'a') as file:
            file.write(f"{name}, {age}\n")
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Function to read user data from a file
def read_user_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
            return data
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Main program logic
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")

    # Validate input
    if not user_age.isdigit():
        print("Error: Age must be a number.")
    else:
        # Save data to file
        save_user_data("user_data.txt", user_name, int(user_age))

        # Read and display data from file
        users = read_user_data("user_data.txt")
        print("Users in file:")
        for user in users:
            print(user.strip())

"""The Python script above includes basic testing and error handling. Testing in this case involves validating:

1.   The ability to save and read data correctly from the file
2.   Handling invalid inputs (e.g., age is not a number).
3.   Dealing with missing files (e.g., file not found errors).
"""

# Test case: Invalid input for age (non-numeric)
user_name = "John"
user_age = "twenty"  # Invalid age input

if not user_age.isdigit():
    print("Error: Age must be a number.")
else:
    save_user_data("test_data.txt", user_name, user_age)