# Dictionary to store student records
students = {}


def add_student(name, age, grade, subjects):
    if name not in students.keys():
        students[name] = {"Age": age, "Grade": grade, "Subjects": subjects}
    return students


def update_student(name):
    if name not in students.keys():
        print("Student name not in record!")
    else:
        print(f"Which field would you need to be updated?")
        user_choice = input("Enter your choice - age, grade, subject: ")
        if user_choice == "age":
            age = int(input("Enter student's age: "))
            students[name]["Age"] = age
        elif user_choice == "grade":
            grade = float(input("Enter student's grade: "))
            students[name]["Grade"] = grade
        elif user_choice == "subject":
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            students[name]["Subjects"] += subjects
    return students


def delete_student(name):
    if name not in students.keys():
        print("Student name not in record!")
    else:
        del students[name]
        return students


def search_student(name):
    if name not in students.keys():
        print("Student name not in record.")
    else:
        print(f"{name}'s record: {students[name]}")
        return students


def list_all_students():
    if students:
        for key in students.keys():
            print(f"{key}'s record: {students[key]}")
        return students
    else:
        print("No students in record!")


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student name to update
            name = input("Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input("Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input("Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
