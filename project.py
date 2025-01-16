from tkinter import *
from functools import partial
from PIL import Image, ImageTk
from student import StudentInfo
from search_student import Search
from menu import MainMenu
from add_student import AddStudent
from print_all_student import PrintAllStudent

HOGWARTS_GOLD = "#D4AF37"
HOGWARTS_BURGUNDY = "#740001"
DARK_GRAY = "#2A2D34"
PARCHMENT = "#FFF1D0"

win = Tk()
win.title("Hogwarts School Management System")
win.configure(bg=DARK_GRAY)
btns = []; container = []
btn_txt = ["Student Profile", "Search Student", "Register Student", "All Students", "Exit Portal"]

try:
    hogwarts_logo = ImageTk.PhotoImage(Image.open("images/hogwarts_logo.png").resize((150, 150)))
    bg_texture = ImageTk.PhotoImage(Image.open("images/parchment_bg.png").resize((1280, 800)))
except:
    print("Please add the required images to the 'images' folder")
    hogwarts_logo = None
    bg_texture = None

student = StudentInfo()
search, addStudent, printAll = Search(student), AddStudent(student), PrintAllStudent(student)
menu = MainMenu(search, addStudent, printAll)

attempts_remaining = 3

def login_confirm():
    global attempts_remaining
    student_id = login_entry.get()
    result = search.verify_login(student_id)
    
    if result:
        global current_student
        current_student = result
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        show_my_info()
        attempts_remaining = 3
    else:
        attempts_remaining -= 1
        if attempts_remaining > 0:
            login_error.config(text=f"Invalid Hogwarts ID - Access Denied\n{attempts_remaining} attempts remaining")
        else:
            login_error.config(text="Too many failed attempts.\nPortal access locked.")
            login_entry.config(state='disabled')
            login_btn.config(state='disabled')
        
        
def show_my_info():
    global current_student
    if not current_student:
        return
        
    for widget in container[0].winfo_children():
        widget.destroy()
    
    title = "=" * 15 + " Student Profile " + "=" * 15
    Label(container[0], text=title, font=("Papyrus", 18, "bold"), bg="#FFF1D0", fg="#740001").grid(row=0, column=0, columnspan=5, pady=5)


    form_frame = Frame(container[0], bg="#740001", padx=2, pady=2)
    form_frame.grid(row=2, column=0, columnspan=5, padx=20, pady=10)
    inner_frame = Frame(form_frame, bg="#FFF1D0", padx=20, pady=10)
    inner_frame.pack(expand=True, fill="both")
    
    labels = ["Name:", "Age:", "Student ID:", "Email Address:", "Phone Number:"]
    for i in range(len(labels)):
        Label(inner_frame, text=labels[i], font=("Courier", 15, "bold"), 
              bg="#FFF1D0", width=14, anchor="w").grid(row=i, column=0, pady=5)
        Label(inner_frame, text=current_student[i], font=("Courier", 15), 
              bg="#FFF1D0", anchor="w", width=30).grid(row=i, column=1, pady=5, padx=10)

    empty_row = Label(inner_frame, text="", bg="#FFF1D0")
    empty_row.grid(row=len(labels), column=0, pady=5)

def logout_confirm():
    global attempts_remaining, current_student
    # Reset login form
    login_entry.config(state='normal')
    login_btn.config(state='normal')
    login_entry.delete(0, END)
    login_error.config(text="")
    attempts_remaining = 3
    current_student = None
    
    for widget in container[0].winfo_children():
        widget.destroy()
    for widget in container[1].winfo_children():
        widget.destroy()
    for widget in container[2].winfo_children():
        widget.destroy()
    for widget in container[3].winfo_children():
        widget.destroy()
        
    search.show_search_ui(container[1])
    addStudent.show_reg_ui(container[2])
    printAll.show_all_students_ui(container[3])
    
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def open_frame(frame_open, close):
    for i in range(len(close)):
        if close[i].winfo_ismapped(): 
            close[i].pack_forget()
    frame_open.pack(side="right", fill="x")

#login_frame
login_frame = Frame(win, bg=DARK_GRAY)
login_frame.pack(fill="both", expand=True)
login_form = Frame(login_frame, bg=DARK_GRAY, padx=40, pady=40)
login_form.place(relx=0.5, rely=0.5, anchor="center")

if hogwarts_logo:
    Label(login_form, image=hogwarts_logo, bg=DARK_GRAY).pack(pady=20)

Label(login_form, text="Hogwarts Student Portal", font=("Papyrus", 24, "bold"), 
      fg=HOGWARTS_GOLD, bg=DARK_GRAY).pack()
Label(login_form, text="Present Your Student ID:", font=("Papyrus", 14), 
      fg=HOGWARTS_GOLD, bg=DARK_GRAY).pack(pady=15)

entry_frame = Frame(login_form, bg=HOGWARTS_GOLD, padx=2, pady=2)
entry_frame.pack(pady=5)
login_entry = Entry(entry_frame, width=20, font=("Arial", 12), bg=PARCHMENT)
login_entry.pack()

login_error = Label(login_form, text="", fg="red", font=("Arial", 10), bg=DARK_GRAY)
login_error.pack(pady=10)

login_btn = Button(login_form, text="Enter", bg=HOGWARTS_BURGUNDY, fg=HOGWARTS_GOLD,
                  width="20", font=("Papyrus", 12, "bold"), relief="raised",
                  activebackground=HOGWARTS_GOLD, activeforeground=HOGWARTS_BURGUNDY)
exit_btn = Button(login_form, text="Disapparate", bg=DARK_GRAY, fg=HOGWARTS_GOLD,
                 width="20", font=("Papyrus", 12, "bold"), relief="raised",
                 activebackground=HOGWARTS_GOLD, activeforeground=DARK_GRAY)
login_btn.pack(pady=10)
exit_btn.pack(pady=10)
login_btn.config(command=login_confirm)
exit_btn.config(command=win.destroy)

#main_frame
main_frame = Frame(win, bg=DARK_GRAY)
menu_contain = Frame(main_frame, border=0, bg=DARK_GRAY)
menu_contain.pack(side="left", fill="y")
content_frame = Frame(main_frame, border=0, bg=PARCHMENT)
content_frame.pack(side="right", fill="both", expand=True)

menu_header = Label(menu_contain, text="Marauder's\nMap", font=("Papyrus", 24, "bold"), 
                   bg=DARK_GRAY, fg=HOGWARTS_GOLD, pady=20)
menu_header.grid(row=0, column=0, pady=(10, 20))

if bg_texture:
    bg_label = Label(content_frame, image=bg_texture)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()  # Push it to the back

for i in range(len(btn_txt)-1):
    container.append(Frame(content_frame, bg=PARCHMENT, pady=8))
    #title
    Label(container[i], text="=" * 15 + " " + btn_txt[i] + " " + "=" * 15, font=("Papyrus", 18, "bold"), 
          bg=PARCHMENT, fg=HOGWARTS_BURGUNDY, width=45, anchor="center").grid(row=0, column=0, columnspan=5)

func = [partial(open_frame, container[0], [container[1], container[2], container[3]]),
        partial(open_frame, container[1], [container[0], container[2], container[3]]),
        partial(open_frame, container[2], [container[1], container[0], container[3]]),
        partial(open_frame, container[3], [container[1], container[2], container[0]]),
        logout_confirm]

for i in range(len(btn_txt)):
    btns.append(Button(menu_contain, border=1, bg=HOGWARTS_BURGUNDY, fg=HOGWARTS_GOLD,
                      width=24, text=btn_txt[i], font=("Papyrus", 18, "bold"),
                      activebackground=HOGWARTS_GOLD, activeforeground=HOGWARTS_BURGUNDY))
    btns[i].grid(row=i+1, column=0, pady=2, padx=5)
    btns[i].config(command=func[i])


search.show_search_ui(container[1])
addStudent.show_reg_ui(container[2])
printAll.show_all_students_ui(container[3])

win.geometry(f"1300x700+300+100")
win.maxsize(1300, 700)
win.minsize(1300, 700)
win.mainloop()