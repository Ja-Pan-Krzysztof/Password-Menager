import tkinter as tk
from tkinter import messagebox

import hashlib

from PasswordMenager import PasswordMenager


class AddMainPass(tk.Tk):
    def __init__(self):
        self.password = None
        self.is_close = True
        super(AddMainPass, self).__init__()

        self.title('Create New Password')
        self.geometry('300x120')
        self.eval('tk::PlaceWindow . center')
        self.configure(background='pink')
        self.resizable(False, False)
        self.iconbitmap('Gui/fortnite.ico')
        self.attributes('-toolwindow', True)

        self.t_frame = tk.Frame(self, bg='pink', width=300, height=80)
        self.t_frame.pack(side=tk.TOP)

        self.b_frame = tk.Frame(self, bg='pink', width=300, height=30)
        self.b_frame.pack(side=tk.BOTTOM)

        self.l_frame = tk.Frame(self.t_frame, bg='pink', width=135, height=90)
        self.l_frame.pack(side=tk.LEFT)

        self.r_frame = tk.Frame(self.t_frame, bg='pink', width=135, height=90)
        self.r_frame.pack(side=tk.RIGHT)

        self.label1 = tk.Label(self.l_frame, text='Enter new a password : ', bg='pink')
        self.label1.place(width=120, height=30, x=5, y=5)
        self.label2 = tk.Label(self.l_frame, text='Repeat a password', bg='pink')
        self.label2.place(width=120, height=30, x=5, y=52)

        self.enter1 = tk.Entry(self.r_frame, bd=1, relief=tk.SOLID, show='*')
        self.enter1.place(width=120, height=30, x=5, y=5)
        self.enter2 = tk.Entry(self.r_frame, bd=1, relief=tk.SOLID, show='*')
        self.enter2.place(width=120, height=30, x=5, y=50)

        self.button_close = tk.Button(self.b_frame, text='Close', relief=tk.SOLID, bd=1, command=self.close)
        self.button_close.place(width=50, height=20, y=5, x=185)

        self.button_ok = tk.Button(self.b_frame, text='Ok', relief=tk.SOLID, bd=1, command=self.ok)
        self.button_ok.place(width=50, height=20, y=5, x=240)

    def close(self):
        self.is_close = True
        self.destroy()
        self.quit()

    def ok(self):
        self.is_close = False
        if self.enter1.get() == self.enter2.get():
            pm = PasswordMenager()
            pm.create_key('main.key')

            with open('pass.txt', 'w') as f:
                password = hashlib.sha1(str(self.enter1.get()).encode())
                f.write(password.hexdigest())

            self.destroy()
            self.quit()

        else:
            messagebox.showerror(title='bad Passwords', message='These passwords aren\'t the same!')
            self.password = self.enter1.get()
