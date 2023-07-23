
# Ask the user how many students are registering
num_students = int(input("How many students are registering? "))

# Create a for loop that runs for that number of students
for i in range(1, num_students + 1):
    # Ask the student to enter their ID number
    student_id = input(f"Enter ID number for student {i}: ")

    # Write the ID number to the text file
    with open("reg_form.txt", "a") as file:
        file.write(f"Student ID: {student_id}\n")
        file.write("--------------------\n")  # Dotted line for signature

print("Registration completed. The details have been saved to reg_form.txt.")
