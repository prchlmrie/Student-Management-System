from tkinter import *

class PrintAllStudent:
    def __init__(self, student):
        self.student_data = student
        self.text_widget = None 

    def print_all_students(self):
        print("\n", "=" * 15, "All Students' Information", "=" * 15)
        for student in self.student_data.allstudents:
            print(f"\nName: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail Address: {student[3]}\nPhone Number: {student[4]}\n")
        print("=" * 15, "Nothing Follows", "=" * 15, "\n")

    def show_all_students_ui(self, container):
        for widget in container.winfo_children():
            widget.destroy()

        title = "=" * 15 + " All Students' Information " + "=" * 15
        Label(container, text=title, font=("Papyrus", 16), bg="#FFF1D0", fg="#740001").grid(row=0, column=0, columnspan=5, pady=5)
        
        refresh_btn = Button(container, text="Refresh List", bg="#740001", fg="#D4AF37",
                           font=("Papyrus", 12, "bold"), command=lambda: self.refresh_list(),
                           activebackground="#D4AF37", activeforeground="#740001")
        refresh_btn.grid(row=1, column=0, columnspan=5, pady=5)
        
        text_frame = Frame(container, bg="#740001", padx=2, pady=2)
        text_frame.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
        
        self.text_widget = Text(text_frame, font=("Courier", 12), bg="white", fg="black", wrap=WORD)
        self.text_widget.pack(expand=True, fill="both", padx=5, pady=5)

        self.refresh_list()

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(2, weight=1)  

    def refresh_list(self):
        if self.text_widget:  
            self.text_widget.configure(state='normal')
            self.text_widget.delete(1.0, END)
            
            if self.student_data.allstudents:  
                for student in self.student_data.allstudents:
                    try:
                        self.text_widget.insert(END, f"\nName: {student[0]}\n")
                        self.text_widget.insert(END, f"Age: {student[1]}\n")
                        self.text_widget.insert(END, f"ID Number: {student[2]}\n")
                        self.text_widget.insert(END, f"Email Address: {student[3]}\n")
                        self.text_widget.insert(END, f"Phone Number: {student[4]}\n")
                    except IndexError:
                        print(f"Error: Invalid student data format: {student}")
                        continue
            else:
                self.text_widget.insert(END, "\nNo students registered yet.\n")
            
            self.text_widget.configure(state='disabled')
