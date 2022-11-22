from tkinter import *
from tkinter import messagebox
import ast
from src import form_checker


window = Tk()
window.title('Sign Up')
window.geometry('925x600+300+200')
window.configure(bg='#fff')
window.resizable(False, False)


def signup():
    username = user.get()
    name_user = name.get()
    email_user = email.get()
    date_birth_user = date_birth.get()
    card_number_user = card_number.get()
    cvv_user = cvv.get()
    exp_date_user = exp_date.get()
    password = password_user.get()
    confirm_password = confirm_code.get()

    if password == confirm_password and (form_checker.usernameChecker(str(user.get()))) and (form_checker.nameChecker(str(name.get()))) and (form_checker.checkEmail(str(email.get()))[0]) and (form_checker.birthDateChecker(str(date_birth.get()))[0]) and (form_checker.cardChecker(str(card_number.get()))[0]) and (form_checker.checkCVV(str(cvv.get()))[0]) and (form_checker.validExpDate(str(exp_date.get()))[0]):
        try:
            file = open('database.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: (name_user, email_user, date_birth_user, card_number_user, cvv_user, exp_date_user, password)}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('database.txt', 'w')
            w = file.write(str(r))

            messagebox.showinfo('Sign Up', 'Sign Up Successful')
            file.close()
        except:
            file = open('database.txt', 'w')
            pp = str({username: (name_user, email_user, date_birth_user, card_number_user, cvv_user, exp_date_user, password)})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Error', 'Password and Confirm Password must be same')

    window.destroy()
    import signin


def signin_command():
    window.destroy()
    import signin


# Image of Sign Up
img = PhotoImage(file='./imgs/signup.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=120)

# Main Label with the input frames
frame = Frame(window, width=400, height=600, bg='#fff')
frame.place(x=480, y=0)

# Sign Up Label
heading = Label(frame, text='Sign Up', font=('Segoe UI', 23, 'bold'), bg='white', fg='#57a1f8')
heading.place(x=100, y=2)


# Username Entry
def on_enter(e):
    label = Label(frame, text='---------------------------------------------------------------------', font=('Segoe UI', 9), bg='white', fg='white')
    label.place(x=25, y=87)
    user.delete(0, 'end')



def on_leave(e):
    if form_checker.usernameChecker(str(user.get())):
        label = Label(frame, text='Valid username!', font=('Segoe UI', 9), bg='white', fg='green')
        label.place(x=25, y=87)
    if not form_checker.usernameChecker(str(user.get())):
        label = Label(frame, text='Usernames must contain 8 characters at least (max: 15)', font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=87)
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
    label = Label(frame, text='---------------------------------------------------------', font=('Segoe UI', 9),
                  bg='white', fg='white')
    label.place(x=25, y=142)
    name.delete(0, 'end')


def on_leave(e):
    if form_checker.nameChecker(str(name.get())):
        label = Label(frame, text='Valid name!', font=('Segoe UI', 9), bg='white', fg='green')
        label.place(x=25, y=142)
    if not form_checker.nameChecker(str(name.get())):
        label = Label(frame, text='Invalid name, please enter a correct name', font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=142)
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
    label = Label(frame, text='-------------------------------------------------------------------',
                  font=('Segoe UI', 9),
                  bg='white', fg='white')
    label.place(x=25, y=197)
    email.delete(0, 'end')


def on_leave(e):
    if email.get() == '':
        email.insert(0, 'Email')
    validation, message = form_checker.checkEmail(str(email.get()))
    if validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='green')
        label.place(x=25, y=197)
    elif not validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=197)


email = Entry(frame, width=30, border=0, font=('Segoe UI', 11), bg='white', fg='black')
email.place(x=30, y=165)
email.insert(0, 'Email')
email.bind("<FocusIn>", on_enter)
email.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=192)


# Date of Birth Entry
def on_enter(e):
    label = Label(frame, text='-------------------------------------------------------------------', font=('Segoe UI', 9),
                  bg='white', fg='white')
    label.place(x=25, y=253)
    date_birth.delete(0, 'end')


def on_leave(e):
    if date_birth.get() == '':
        date_birth.insert(0, 'Date of Birth')
    validation, message = form_checker.birthDateChecker(str(date_birth.get()))
    if validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='green')
        label.place(x=25, y=253)
    elif not validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=253)


date_birth = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
date_birth.place(x=30, y=220)
date_birth.insert(0, 'Date of Birth')
date_birth.bind("<FocusIn>", on_enter)
date_birth.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)


# Card Number - Credit Card Entry
def on_enter(e):
    label = Label(frame, text='-------------------------------------------------------------------',
                  font=('Segoe UI', 9),
                  bg='white', fg='white')
    label.place(x=25, y=307)
    card_number.delete(0, 'end')


def on_leave(e):
    if card_number.get() == '':
        card_number.insert(0, 'Card Number')
    validation, message = form_checker.cardChecker(str(card_number.get()))
    if validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='green')
        label.place(x=25, y=307)
    elif not validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=307)


card_number = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
card_number.place(x=30, y=275)
card_number.insert(0, 'Card Number')
card_number.bind("<FocusIn>", on_enter)
card_number.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=302)


# Security Code - Credit Card Entry
def on_enter(e):
    label = Label(frame, text='------------------------',
                  font=('Segoe UI', 9),
                  bg='white', fg='white')
    label.place(x=25, y=362)
    cvv.delete(0, 'end')


def on_leave(e):
    if cvv.get() == '':
        cvv.insert(0, 'CVV')
    validation, message = form_checker.checkCVV(str(cvv.get()))
    if validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='green')
        label.place(x=25, y=362)
    elif not validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=362)


cvv = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
cvv.place(x=30, y=330)
cvv.insert(0, 'CVV')
cvv.bind("<FocusIn>", on_enter)
cvv.bind("<FocusOut>", on_leave)

Frame(frame, width=137, height=2, bg='black').place(x=25, y=357)


# Exp Date - Credit Card Entry
def on_enter(e):
    label = Label(frame, text='---------------------------------',
                  font=('Segoe UI', 9),
                  bg='white', fg='white')
    label.place(x=182, y=362)
    exp_date.delete(0, 'end')


def on_leave(e):
    if exp_date.get() == '':
        exp_date.insert(0, 'EXP Date')
    validation, message = form_checker.validExpDate(str(exp_date.get()))
    if validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='green')
        label.place(x=182, y=362)
    elif not validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=182, y=362)


exp_date = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
exp_date.place(x=187, y=330)
exp_date.insert(0, 'EXP Date')
exp_date.bind("<FocusIn>", on_enter)
exp_date.bind("<FocusOut>", on_leave)

Frame(frame, width=137, height=2, bg='black').place(x=182, y=357)


# Password Entry
def on_enter(e):
    label = Label(frame, text='---------------------------------------------------------', font=('Segoe UI', 9),
                  bg='white', fg='white')
    label.place(x=25, y=417)
    password_user.delete(0, 'end')


def on_leave(e):
    if password_user.get() == '':
        password_user.insert(0, 'Password')
    validation, message = form_checker.passwordChecker(str(password_user.get()))
    if validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='green')
        label.place(x=25, y=417)
    elif not validation:
        label = Label(frame, text=message, font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=417)


password_user = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
password_user.place(x=30, y=385)
password_user.insert(0, 'Password')
password_user.bind("<FocusIn>", on_enter)
password_user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=412)


# Confirm Password Entry
def on_enter(e):
    label = Label(frame, text='---------------------------------------------------------', font=('Segoe UI', 9),
                  bg='white', fg='white')
    label.place(x=25, y=472)
    confirm_code.delete(0, 'end')


def on_leave(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm Password')
    password = password_user.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        label = Label(frame, text='Password Matched', font=('Segoe UI', 9), bg='white', fg='green')
        label.place(x=25, y=472)
    elif password != confirm_password:
        label = Label(frame, text='Password Not Matched', font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=472)


confirm_code = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
confirm_code.place(x=30, y=440)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=467)

# Sign Up Button and Sign In Button
Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', cursor='hand2', border=0, command=signup).place(x=35, y=500)
label = Label(frame, text='Already have an account?', font=('Segoe UI', 9), bg='white', fg='black')
label.place(x=70, y=550)

signin = Button(frame, text='Sign In', width=6, bg='white', fg='#57a1f8', border=0, cursor='hand2',
                command=signin_command)
signin.place(x=240, y=550)

# Execute the window
window.mainloop()
