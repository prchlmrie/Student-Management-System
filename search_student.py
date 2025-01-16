from tkinter import *
from tkinter import messagebox

class Search:
    def __init__(self, student):
        self.student_data = student

    def search_student(self, studentId):
        for student in self.student_data.allstudents: 
            if student[2] == studentId: 
                return student
        return None

    def verify_login(self, studentID):
        if not studentID:
            return False
        for student in self.student_data.allstudents:
            if student[2] == studentID:  
                return student  
        return False

    def show_search_ui(self, search_frame):
        title = "=" * 15 + " Search Student " + "=" * 15
        Label(search_frame, text=title, font=("Papyrus", 18, "bold"), 
              bg="#FFF1D0", fg="#740001").grid(row=0, column=0, columnspan=3, pady=5)
        
        form_frame = Frame(search_frame, bg="#740001", padx=2, pady=2)
        form_frame.grid(row=2, column=0, columnspan=3, padx=(150, 150), pady=10)
        
        inner_frame = Frame(form_frame, bg="#FFF1D0", padx=20, pady=10)
        inner_frame.pack(expand=True, fill="both")
        
        Label(inner_frame, text="Student ID Number:", font=("Arial", 15, "bold"), 
              bg="#FFF1D0").grid(row=0, column=0, pady=(8,2))
        
        self.search_entry = Entry(inner_frame, width=30, font=("Arial", 15))
        self.search_entry.grid(row=1, column=0, pady=(2,8))
        
        search_btn = Button(inner_frame, text="Search", bg="#740001", fg="#D4AF37",
                           width="20", font=("Papyrus", 15, "bold"),
                           activebackground="#D4AF37", activeforeground="#740001",
                           command=self.perform_search)
        search_btn.grid(row=2, column=0, pady=10)

        self.result_frame = Frame(search_frame, bg="#FFF1D0")
        self.result_frame.grid(row=3, column=0, columnspan=3, pady=10, padx=50)

    def perform_search(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        student_id = self.search_entry.get()
        if not student_id:
            messagebox.showerror("Error", "Please enter a Student ID")
            return

        result = self.search_student(student_id)
        if result:
            Label(self.result_frame, text="Search Result:", font=("Papyrus", 16, "bold"),
                  bg="#FFF1D0", fg="#740001").pack(anchor="w", padx=(0,0), pady=(10,5))
            
            form_frame = Frame(self.result_frame, bg="#740001", padx=2, pady=2)
            form_frame.pack(padx=(0,20), pady=10, anchor="e") 

            inner_frame = Frame(form_frame, bg="#FFF1D0", padx=20, pady=10)
            inner_frame.pack(expand=True, fill="both")
            
            labels = ["Name:", "Age:", "ID Number:", "Email Address:", "Phone Number:"]
            for i in range(len(labels)):
                Label(inner_frame, text=labels[i], font=("Arial", 15, "bold"), 
                    bg="#FFF1D0", width=13, anchor="e").grid(row=i, column=0, pady=5)
                Label(inner_frame, text=result[i], font=("Arial", 15), 
                    bg="#FFF1D0", anchor="w").grid(row=i, column=1, pady=5, padx=10)
        else:
            Label(self.result_frame, text=f"No student found with ID: {student_id}", 
                font=("Arial", 15), fg="red", bg="#FFF1D0").pack(pady=10)