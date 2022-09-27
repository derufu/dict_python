def again():
    students = {'Jo' : 77, 'Jojo' : 74, 'Joe' : 93}
    option = input(f"'a' for adding, 'd' for deleting, and 'e' for end/termination of the program  => ")
    if option == 'a':
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        students[name] = grade
        print(students)
        again()
    if option == 'b':
        name = input("Enter Name: ")
        if name == "":
            print("Record Empty!")
            again()
        else:
            del students[name]
            print(students)
    if option == 'e':
        print("Thank you!")
again()