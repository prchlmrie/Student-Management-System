from tkinter import *
from functools import partial
from tkinter import messagebox

class AddStudent:
    def __init__(self, student):
        self.student_data = student

    def add_student(self, name, age, idnum, email, phone):
        self.student_data.set_name(name)
        self.student_data.set_age(age)
        self.student_data.set_idnum(idnum)
        self.student_data.set_email(email)
        self.student_data.set_phone(phone)
        student_info = [name, age, idnum, email, phone]
        self.student_data.allstudents.append(student_info)
        print(f"Added student {student_info[0]} to the list.")
        student_info = f"{name}, {age}, {idnum}, {email}, {phone}"
        self.write_to_file(student_info)

    def write_to_file(self, student_info):
        with open("student_data.txt", "a+") as file:
            for x in student_info:
                file.write(f"{x}")
            file.write("\n")
            file.close()
        print("Student data saved successfully.")

    def gather_details(self):
        print("\n","="*15, "Add New Student", "="*15)
        name, age, idnum, email, phone = input("Enter student's name: "), input("Enter student's age: "), input("Enter student's ID number: "), input("Enter student's email: "), input("Enter student's phone: ")
        print("=" * 15, " Nothing Follows ", "=" * 15,"\n")
        self.add_student(name, age, idnum, email, phone)
    
    def show_reg_ui(self, reg_frame):

        title = "=" * 15 + " Register Student " + "=" * 15
        Label(reg_frame, text=title, font=("Papyrus", 18, "bold"), 
              bg="#FFF1D0", fg="#740001").grid(row=0, column=0, columnspan=5, padx=(0, 150), pady=5)

        self.lblErrors = Label(reg_frame, text="", fg="red", bg="#FFF1D0", 
                          font=("Arial", 12), justify="center") 
        self.lblErrors.grid(row=1, column=0, columnspan=5, pady=5, padx=(0, 150), sticky="nsew") 

        form_frame = Frame(reg_frame, bg="#740001", padx=2, pady=2)
        form_frame.grid(row=2, column=0, columnspan=5, padx=(0, 170), pady=10)
    
        inner_frame = Frame(form_frame, bg="#FFF1D0", padx=20, pady=10)
        inner_frame.pack(expand=True, fill="both")
        
    
        self.reg_txt = ["Name", "Age", "Student ID", "Email Address", "Phone Number"]
        self.reg_entry = []
    
        for i in range(len(self.reg_txt)):
            Label(inner_frame, text=self.reg_txt[i], font=("Arial", 15, "bold"), 
                  bg="#FFF1D0", width=13, anchor="e").grid(row=i, column=0, pady=8)
            self.reg_entry.append(Entry(inner_frame, width=30, font=("Arial", 15)))
            self.reg_entry[i].grid(row=i, column=1, pady=8, padx=10)

        empty_row = Label(inner_frame, text="", bg="#FFF1D0")
        empty_row.grid(row=len(self.reg_txt), column=0, pady=5)

        reg_btn = Button(inner_frame, text="Register", bg="#740001", fg="#D4AF37",
                        width="20", font=("Papyrus", 15, "bold"),
                        activebackground="#D4AF37", activeforeground="#740001",
                        command=self.check_entries)
        reg_btn.grid(row=len(self.reg_txt)+1, column=0, columnspan=2, pady=10)

    def check_entries(self):
        errors = []
        import re
        
        for i in range(len(self.reg_entry)):
            if self.reg_entry[i].get().strip() == "":
                errors.append(f"• {self.reg_txt[i]}")
        
        if not errors:
            try:
                age = int(self.reg_entry[1].get())
                if age <= 0:
                    errors.append("• Age must be greater than 0")
            except ValueError:
                errors.append("• Age must be a valid number")
            
            email = self.reg_entry[3].get().strip()
            for student in self.student_data.allstudents:
                if student[3].lower() == email.lower():
                    errors.append("• Email address already exists")
                    break

        if not errors:
            self.add_student(
                self.reg_entry[0].get().strip(), 
                self.reg_entry[1].get().strip(), 
                self.reg_entry[2].get().strip(), 
                self.reg_entry[3].get().strip(), 
                self.reg_entry[4].get().strip()
            )
            messagebox.showinfo(title="Success", message="Student added successfully.")
            for entry in self.reg_entry:
                entry.delete(0, END)
            self.lblErrors.config(text="")  
        else:
            error_message = "Please fill in the following required fields:\n" + "\n".join(errors)
            self.lblErrors.config(text=error_message)
