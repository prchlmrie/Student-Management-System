import os

class MainMenu:
    def __init__(self, search, addStudent, printAll): # initialize attributes
        self.search = search
        self.addStudent = addStudent
        self.printAll = printAll

    def main_menu(self, user):
        while True:
            os.system("cls")
            print(f"Welcome, Admin {user[0]}!\n", "="*15,"Main Menu","="*15)
            print("1. View your information\n2. View other student's information\n3. Register a new student\n4. Print all students in the system\n5. Exit")
            choice = input("Your choice: ")
            if choice == '1':
                os.system("cls")
                self.search.search_student(user[2])
                input("Go back (Press Enter).")
            elif choice == '2':
                self.search_student_option()
            elif choice == '3':
                self.add_student_option()
            elif choice == '4':
                self.printAll.print_all_students()
                input("Go back (Press Enter).")
            else:
                os.system("cls")
                print("\n", "="*5, "Exiting the system. Goodbye!", "="*5, "\n")
                break
