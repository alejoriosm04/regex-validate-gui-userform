from tkinter import *
import ast

root = Tk()
root.title('Sign In')
root.geometry('925x600+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    file = open('database.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:
        root.destroy()
        import user_info

    else:
        label = Label(frame, text='Wrong Username!', font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=110)

        label = Label(frame, text='Wrong Password!', font=('Segoe UI', 9), bg='white', fg='red')
        label.place(x=25, y=180)

def signup_command():
    root.destroy()
    import signup


img = PhotoImage(file='signin.png')
Label(root, image=img, bg='white').place(x=50, y=120)

frame = Frame(root, width=350, height=350, bg='#fff')
frame.place(x=480, y=120)

heading = Label(frame, text='Sign in', font=('Segoe UI', 23, 'bold'), bg='white', fg='#57a1f8')
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, border=0, font=('Segoe UI', 11), bg='white', fg='black')
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', cursor='hand2', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text='Forgot Password?', font=('Segoe UI', 9), bg='white', fg='black')
label.place(x=75, y=270)

sign_up = Button(frame, width=6, cursor='hand2', text='Sign Up', bg='white', fg='#57a1f8', border=0, command=signup_command)
sign_up.place(x=215, y=270)

root.mainloop()
