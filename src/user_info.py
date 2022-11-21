from tkinter import *
import ast
from src import form_checker


def data(username, password):
    window = Tk()
    window.title('User Info')
    window.geometry('925x600+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    file = open('database.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)

    name = r[username][0]
    email = r[username][1]
    date_of_birth = r[username][2]
    days_left = form_checker.tillYourBirthday(form_checker.getDayMonthYear(date_of_birth)[0], form_checker.getDayMonthYear(date_of_birth)[1], form_checker.getDayMonthYear(date_of_birth)[2])
    credit_card = r[username][3]
    cvv = r[username][4]
    exp_date = r[username][5]


    img = PhotoImage(file='user_info.png')
    Label(window, image=img, bg='white').place(x=50, y=120)

    frame = Frame(window, width=400, height=600, bg='#fff')
    frame.place(x=480, y=0)

    heading = Label(frame, text='Your Profile', font=('Segoe UI', 23, 'bold'), bg='white', fg='#57a1f8')
    heading.place(x=100, y=5)

    name = Label(frame, text=f'Welcome {name}!', font=('Segoe UI', 15, 'bold'), bg='white', fg='#57a1f8')
    name.place(x=30, y=80)
    Frame(frame, width=310, height=2, bg='black').place(x=30, y=115)

    email = Label(frame, text=f'Email: {email}', font=('Segoe UI', 10, 'bold'), bg='white', fg='black')
    email.place(x=30, y=130)

    dob = Label(frame, text=f'Your Happy Bithday is in {date_of_birth}', font=('Segoe UI', 12, 'bold'), bg='white', fg='#88b000')
    dob.place(x=30, y=200)

    days_left = Label(frame, text=days_left, font=('Segoe UI', 12, 'bold'), bg='white', fg='#88b000')
    days_left.place(x=30, y=230)

    credit_card = Label(frame, text=f'Credit Card: {credit_card}', font=('Segoe UI', 10, 'bold'), bg='white', fg='black')
    credit_card.place(x=30, y=300)

    cvv = Label(frame, text=f'CVV: {cvv}', font=('Segoe UI', 10, 'bold'), bg='white', fg='black')
    cvv.place(x=30, y=350)

    exp_date = Label(frame, text=f'Exp Date: {exp_date}', font=('Segoe UI', 10, 'bold'), bg='white', fg='black')
    exp_date.place(x=30, y=400)

    window.mainloop()
