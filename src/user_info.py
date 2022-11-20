from tkinter import *
import ast

window = Tk()
window.title('User Info')
window.geometry('925x600+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

img = PhotoImage(file='user_info.png')
Label(window, image=img, bg='white').place(x=50, y=120)

frame = Frame(window, width=350, height=350, bg='#fff')
frame.place(x=480, y=120)

heading = Label(frame, text='Your Profile', font=('Segoe UI', 23, 'bold'), bg='white', fg='#57a1f8')
heading.place(x=100, y=5)

window.mainloop()
