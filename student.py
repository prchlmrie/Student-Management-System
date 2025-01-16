class StudentInfo:
    def __init__(self):
        self.name, self.age, self.idnum, self.email, self.phone = "","","","",""
        self.allstudents = []
        self.read_file()

    # Getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_idnum(self):
        return self.idnum

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    # Setters
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_idnum(self, idnum):
        self.idnum = idnum

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    # to be used for the format
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID Number: {self.idnum}\nEmail: {self.email}\nPhone Number: {self.phone}\n"

    def read_file(self):
        try:
            with open("student_data.txt", "r") as file:
                lines = file.readlines()
                for line in lines[0:]:
                    student1 = line.strip().split(", ")
                    self.allstudents.append(student1)
            print("Student data added to the list.")
        except FileNotFoundError:
            print("No existing student data found.")