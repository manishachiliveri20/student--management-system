students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        student_id = input("Enter student ID: ")
        course = input("Enter student course: ")

        student = {
            "name": name,
            "age": age,
            "id": student_id,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n===== STUDENT DETAILS =====")
            for student in students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("ID:", student["id"])
                print("Course:", student["course"])
                print("-------------------------")

    elif choice == "3":
        search_id = input("Enter student ID to search: ")
        found = False

        for student in students:
            if student["id"] == search_id:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("ID:", student["id"])
                print("Course:", student["course"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")