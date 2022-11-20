from tkinter import *
from tkinter import messagebox
import ast
import pymongo

window = Tk()
window.title('Sign Up')
window.geometry('925x600+300+200')
window.configure(bg='#fff')
window.resizable(False, False)


def signup():
    username = user.get()
    password = password_user.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            file = open('database.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('database.txt', 'w')
            w = file.write(str(r))

            messagebox.showinfo('Sign Up', 'Sign Up Successful')
        except:
            file = open('database.txt', 'w')
            pp = str({username: password})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Error', 'Password and Confirm Password must be same')


def signin_command():
    window.destroy()
    import signin


# Image of Sign Up
img = PhotoImage(file='signup.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=120)

# Main Label with the input frames
frame = Frame(window, width=400, height=600, bg='#fff')
frame.place(x=480, y=0)

# Sign Up Label
heading = Label(frame, text='Sign Up', font=('Segoe UI', 23, 'bold'), bg='white', fg='#57a1f8')
heading.place(x=100, y=2)


# Username Entry
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
user.place(x=30, y=55)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=82)


# Name Entry
def on_enter(e):
    name.delete(0, 'end')


def on_leave(e):
    if name.get() == '':
        name.insert(0, 'Name')


name = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
name.place(x=30, y=110)
name.insert(0, 'Name')
name.bind("<FocusIn>", on_enter)
name.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=137)


# Email Entry
def on_enter(e):
    email.delete(0, 'end')


def on_leave(e):
    if email.get() == '':
        email.insert(0, 'Email')


email = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
email.place(x=30, y=165)
email.insert(0, 'Email')
email.bind("<FocusIn>", on_enter)
email.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=192)


# Date of Birth Entry
def on_enter(e):
    date_birth.delete(0, 'end')


def on_leave(e):
    if date_birth.get() == '':
        date_birth.insert(0, 'Date of Birth')


date_birth = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
date_birth.place(x=30, y=220)
date_birth.insert(0, 'Date of Birth')
date_birth.bind("<FocusIn>", on_enter)
date_birth.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)


# Card Number -  Credit Card Entry
def on_enter(e):
    card_number.delete(0, 'end')


def on_leave(e):
    if card_number.get() == '':
        card_number.insert(0, 'Card Number')


card_number = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
card_number.place(x=30, y=275)
card_number.insert(0, 'Card Number')
card_number.bind("<FocusIn>", on_enter)
card_number.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=302)


# Security Code -  Credit Card Entry
def on_enter(e):
    cvv.delete(0, 'end')


def on_leave(e):
    if cvv.get() == '':
        cvv.insert(0, 'CVV')


cvv = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
cvv.place(x=30, y=330)
cvv.insert(0, 'CVV')
cvv.bind("<FocusIn>", on_enter)
cvv.bind("<FocusOut>", on_leave)

Frame(frame, width=137, height=2, bg='black').place(x=25, y=357)


# Exp Date -  Credit Card Entry
def on_enter(e):
    exp_date.delete(0, 'end')


def on_leave(e):
    if exp_date.get() == '':
        exp_date.insert(0, 'EXP Date')


exp_date = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
exp_date.place(x=187, y=330)
exp_date.insert(0, 'EXP Date')
exp_date.bind("<FocusIn>", on_enter)
exp_date.bind("<FocusOut>", on_leave)

Frame(frame, width=137, height=2, bg='black').place(x=182, y=357)


# Password Entry
def on_enter(e):
    password_user.delete(0, 'end')


def on_leave(e):
    if password_user.get() == '':
        password_user.insert(0, 'Password')


password_user = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
password_user.place(x=30, y=385)
password_user.insert(0, 'Password')
password_user.bind("<FocusIn>", on_enter)
password_user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=412)


# Confirm Password Entry
def on_enter(e):
    confirm_code.delete(0, 'end')


def on_leave(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm Password')


confirm_code = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
confirm_code.place(x=30, y=440)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=467)

# Sign Up Button and Sign In Button
Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=500)
label = Label(frame, text='Already have an account?', font=('Segoe UI', 9), bg='white', fg='black')
label.place(x=70, y=550)

signin = Button(frame, text='Sign In', width=6, bg='white', fg='#57a1f8', border=0, cursor='hand2',
                command=signin_command)
signin.place(x=240, y=550)

# Execute the window
window.mainloop()
