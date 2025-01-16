# 🧙‍♀️ Hogwarts Student Portal
## Description
This system is a Hogwarts-themed student portal that allows the admin to view, search, add, and see all the information of the students.

## Features
1. Login
2. View Information
3. Search Student
4. Add Student 
5. Print All Student
6. Exit

## Files
### project.py
- This file is the main file that contains the GUI of the program. I have imported each of the files and their main functions, as well as tkinter, which will be used to handle the visualization of the program. I first declared the colors that will be used, such as Hogwarts' famous palette of gold and burgundy. I have imported `PILLOW` in order to display images such as the logo and the parchment background.

- I added a login feature for security purposes, although this is the most basic version I could make. The user will have 3 attempts to log in to the system. This feature will use the students' ID to access the main program, and this will be handled by the `login_confirm` function. Once the user successfully logs in, their own information will immediately appear.

- This GUI simply displays each feature frame by frame, like a stack of cards that forgets the other stacks when a certain stack is shown on the screen.

### student.py
- As the name implies, the **class StudentInfo** handles all of the information of a student. It uses setters and getters as well as an empty list for the `read_file(self)` function later on. It handles data such as name, age, ID number, email, and phone number. I have also added a `__str__(self)` function for formatting the said details. The `read_file(self)` function is responsible for reading the details of the students from the list residing in the student_data.txt file by reading the file one line at a time and splitting it by removing the comma and the trailing space. If no such file exists, the function will return a print statement that raises a `FileNotFoundError` exception.

### add_student.py 
- The **class AddStudent** initializes the `student_data`, which is the text file. It has a method `add_student(self, name, age, idnum, email, phone)` that adds the student to the allstudents list, then calls the `write_to_file(self, student_info)` method to write all of the information to `student_data.txt` in one line, separated by commas. The `gather_details(self)` method is responsible for getting the details of the student such as name, age, ID number, email, and phone number. The `show_reg_ui(self, reg_frame)` method, on the other hand, is responsible for formatting the form that gathers the details of the student. It uses tkinter to do so. The `check_entries(self)` method is the input validator to ensure that the correct information is being provided.

### search_student.py 
- The **class Search** is responsible for searching for a student through the list of students using the student's ID. It matches the input information from the entry then compares it to the student ID in the system. Just like in add_student, the `show_search_ui(self, search_frame)` is responsible for the form where the admin can see the Search Label as well as the entry. The `perform_search(self)` handles the results of the search student ID, whether there is a result or none. This will display at the bottom of the search box in a separate form.

### print_all_student.py
- The **class PrintAllStudents** is responsible for printing all the students in the system. It reads the students' data from the `student_data.txt` file, formats it in a readable way, and then prints it. The `show_all_student_ui(self, container)` handles the form where the list of all the students is shown. I have also added a `refresh_list(self)` method that will refresh the list whenever the admin adds new students to the list.

### menu.py
- The **class MainMenu** initializes the search, add_student, and printAll as this class is responsible for the main menu options showing the different functionalities of this program that the admin will toggle around.

### student_data.txt
- This file simply holds all of the students' information.

## Designs
- I chose a Hogwarts theme as I, myself, am a huge fan of Harry Potter. I initially planned to make it Ravenclaw-themed to showcase my own house; however, I felt like I'd be too limited with colors revolving around blue. I didn't like that, which led me to do Hogwarts instead. I named it the Marauder's Map, inspired by the Marauder Gryffindor boys.

- I use 3 attempts for the login as it is usually a reasonable number of chances to give.

- The menu is put on the left side of the whole frame as it is easy to navigate in that way.

## For Future Improvements
- At some point, I would like to add a database for more security and implement more input validation. I have been working on this project for at least 3 months, starting from October 2023, and hope to improve it soon.