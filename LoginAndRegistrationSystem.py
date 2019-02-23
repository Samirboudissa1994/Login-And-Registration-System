from tkinter import *
import os

def exit():
    screen.destroy()

def secret_info():
    screen3.destroy()
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Secret information")
    screen6.geometry("550x300")
    Label(screen6, text = "You have now accessed the secret information. \n \n This is the first project that i've done myself with Python. \n This project can be found uploaded in Github and can be tested by everyone. \n Thank you for using my program, click 'exit' to shut down the program.").pack()
    Button(screen6, text = "exit", command = exit).pack()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Logged in")
    screen3.geometry("500x300")
    Label(screen3, text = "Logged in successfully, \n click OK to access the secret information").pack()
    Button(screen3, text = "OK", command = secret_info).pack()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Error")
    screen4.geometry("150x100")
    Label(screen4, text = "Password could not be linked to any username").pack()
    Button(screen4, text = "OK", command = delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")
    Label(screen5, text = "We could not find given username from our system").pack()
    Button(screen5, text = "OK", command = delete4).pack()

def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()

    while True:
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess()
                break
            else:
                label_title = Label(screen2, text="Invalid username or password", fg="red", font=("calibri", 11))
                label_title.place(x=135, y=19)
                return
        else:
            label_title = Label(screen2, text="Invalid username or password", fg="red", font=("calibri", 11))
            label_title.place(x=135, y=19)
            return

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x300")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show = '*')
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def registration_complete():
    username_info = username.get()
    password_info = password.get()
    password2_info = password2.get()
    email_info = email.get()
    occupation_info = occupation.get()
    company_info = company.get()
    country_info = c.get()
    gender_info = gender.get()
    skill1_info = skill1.get()
    skill2_info = skill2.get()

    while True:
        if username_info != '' and password_info != '' and password2_info != '' and email_info != '':
            if '@' in email_info:
                if password2_info == password_info:
                    break
                else:
                    label_title = Label(screen1, text="                      Passwords don't match                ", fg="red",font=("calibri", 11))
                    label_title.place(x=40, y=93)
                    return
            else:
                label_title = Label(screen1, text="Please enter a valid email address", fg="red", font=("calibri", 11))
                label_title.place(x=70, y=93)
                return
        else:
            label_title = Label(screen1, text="           Please fill the required fields", fg="red", font=("calibri", 11))
            label_title.place(x=70, y=93)
            return

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.write(email_info+"\n")
    file.write(country_info+"\n")
    file.write(gender_info+"\n")
    file.write(skill1_info+"\n")
    file.write(skill2_info+"\n")
    file.write(company_info+"\n")
    file.write(occupation_info+"\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    confirm_entry.delete(0, END)
    occupation_entry.delete(0, END)
    company_entry.delete(0, END)

    skill1.set(0)
    skill2.set(0)
    gender.set(0)

    label_title = Label(screen1, text="Registration success, you can now log in with your user", fg="green", font=("calibri", 11))
    label_title.place(x=50, y=93)

def register():
    global screen1
    screen1 = Toplevel()
    screen1.geometry("500x600")
    screen1.title("Register")

    global username
    global password
    global email
    global password2
    global c
    global occupation
    global company
    global gender
    global skill1
    global skill2
    global username_entry
    global password_entry
    global email_entry
    global confirm_entry
    global occupation_entry
    global company_entry

    username = StringVar()
    email = StringVar()
    c = StringVar()
    password = StringVar()
    password2 = StringVar()
    occupation = StringVar()
    company = StringVar()
    gender = StringVar()
    skill1 = StringVar()
    skill2 = StringVar()

    label_title = Label(screen1, text = "Create an account", font = ("Calibri", 20))
    label_title.place(x=50, y=3)

    label_title = Label(screen1, text = "Please, fill in the details below in order to register")
    label_title.place(x=90, y=50)

    label_title = Label(screen1, text = "* indicates a required field", fg = "red")
    label_title.place(x=140, y=73)

    label_user = Label(screen1, text ="Username", width = "25")
    label_user.place(x=30, y=130)
    label_required = Label(screen1, text="*", fg = "red")
    label_required.place(x=335, y=130)
    username_entry = Entry(screen1, textvariable = username)
    username_entry.place(x=170, y=130)

    label_email = Label(screen1, text ="Email address", width = "25")
    label_email.place(x=17, y=170)
    label_required2 = Label(screen1, text="*", fg = "red")
    label_required2.place(x=335, y=170)
    email_entry = Entry(screen1, textvariable = email)
    email_entry.place(x=170, y=170)

    label_pass = Label(screen1, text ="Password", width = "25")
    label_pass.place(x=31, y=210)
    label_required2 = Label(screen1, text="*", fg = "red")
    label_required2.place(x=335, y=210)
    password_entry = Entry(screen1, textvariable = password, show = '*')
    password_entry.place(x=170, y=210)

    label_confirm = Label(screen1, text ="Confirm", width = "25")
    label_confirm.place(x=35, y=250)
    label_required2 = Label(screen1, text="*", fg = "red")
    label_required2.place(x=335, y=250)
    confirm_entry = Entry(screen1, textvariable = password2, show = '*')
    confirm_entry.place(x=170, y=250)

    label_occupation = Label(screen1, text ="Occupation", width = "25")
    label_occupation.place(x=26, y=290)
    occupation_entry = Entry(screen1, textvariable = occupation)
    occupation_entry.place(x=170, y=290)

    label_company = Label(screen1, text ="Company", width = "25")
    label_company.place(x=30, y=330)
    company_entry = Entry(screen1, textvariable = company)
    company_entry.place(x=170, y=330)

    countries = ['Finland', 'Sweden', 'Norway']

    droplist=OptionMenu(screen1,c, *countries)
    droplist.config(width=16)
    c.set('Country')
    droplist.place(x=170, y=370)

    label_gender = Label(screen1, text ="Gender", width = "25")
    label_gender.place(x=34, y=410)
    Radiobutton(screen1, text = "Male", padx=0, variable=gender, value="Male") .place( x=170, y=410)
    Radiobutton(screen1, text="Female", padx=10, variable=gender, value="Female") .place(x=250, y=410)

    label_skill = Label(screen1, text="Skills", width="25")
    label_skill.place(x=34, y=450)
    Checkbutton(screen1, text = "Javascript", variable=skill1) .place(x=170, y=450)
    Checkbutton(screen1, text="Python", variable=skill2) .place(x=262, y=450)

    Button(screen1, text="Register", width=20, bg="brown", fg="white", command = registration_complete) .place(x=160, y=490)

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x300")
    screen.title("Login and Registration System")
    Label(text = "Welcome to this program!", width = "300", height = "2", font = ("Calibri", 10)).pack()
    Label(text = "In order to access the secret information \n that i have stored to this program, you need to log in first.", width = "300", height = "2", font = ("Calibri", 10)).pack()
    Label(text = "If you don't have a user, click on the register button to create an account.", width = "300", height = "2", font = ("Calibri", 10)).pack()
    Button(text = "Login", width = "30", height = "2", font = ("Calibri", 13), command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", width = "30", height = "2", font = ("Calibri", 13), command = register).pack()
    Label(text = "").pack()
    screen.mainloop()

main_screen()