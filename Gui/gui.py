import tkinter as tk
from tkinter import messagebox

from functools import partial
import hashlib
import os

from PasswordMenager import PasswordMenager
from Gui.guiAddPassword import AddPassword


class AppGui(tk.Tk):
    def __init__(self):
        super(AppGui, self).__init__()
        self.password_dict = {}
        self.pm = PasswordMenager()

        if not os.path.exists('all.pass'):
            os.system(f'type nul > all.pass')

        self.y_conrinate = self.winfo_screenheight()
        self.x_conrinate = self.winfo_screenwidth()

        self.x_conrinate = (self.x_conrinate / 2) - (800 / 2)
        self.y_conrinate = (self.y_conrinate / 2) - (600 / 2)

        self.title('Password Menager')
        self.geometry(f'800x600+{int(self.x_conrinate)}+{int(self.y_conrinate)}')
        self.configure(background='#FFF5E4')
        self.resizable(False, False)
        self.iconbitmap('Gui/fortnite.ico')

        # frames
        self.l_frame = tk.Frame(self, width=200, height=560, bg='#FFECCE')
        self.l_frame.pack(side=tk.LEFT, padx=20)

        self.r_frame = tk.Frame(self, bg='#FFECCE', height=560, width=300)
        self.r_frame.pack(side=tk.RIGHT, padx=20)

        self.c_frame = tk.Frame(self, bg='#FFF5E4', height=560, width=200)
        self.c_frame.pack(pady=20)

        # labels
        self.site_label = tk.Label(self.l_frame, text='Sites')
        self.site_label.place(height=25, width=190, x=5, y=5)

        self.pass_label = tk.Label(self.r_frame, text='Password')
        self.pass_label.place(height=25, width=290, x=5, y=5)

        self.show_sites()

        self.button_add = tk.Button(self.r_frame, text='Add password', relief=tk.SOLID, bd=1, command=self.add)
        self.button_add.place(width=150, height=30, y=525, x=145)

    def command_button(self, site):
        pg = PassGui(site)
        pg.mainloop()

        if pg.option == 1:
            self.show_password(site)

    def show_sites(self):
        with open('all.pass', 'r') as f:
            for line in f:
                site, password = line.split(':')
                self.password_dict[site] = password

        a = 45
        b = 0
        for key, value in self.password_dict.items():
            site = tk.Button(self.l_frame, text=f'{key}', relief=tk.RIDGE, command=partial(self.command_button, key))
            site.place(height=25, width=190, x=5, y=a)

            a += 27
            b += 1

    def show_password(self, site):
        password = self.pm.get_password(site, 'main.key', 'all.pass')

        tk.Label(
            self.r_frame,
            text=f'{site} : {password}'
        ).place(height=50, width=290, x=5, y=35)

    def add(self):
        ap = AddPassword()
        ap.mainloop()

        if ap.site is not None and ap.password is not None:
            self.pm.add_password(ap.site, ap.password, 'main.key', 'all.pass')

        self.show_sites()


class PassGui(tk.Tk):
    def __init__(self, site: str):
        self.site = site
        self.option = 0
        self.password = None
        super(PassGui, self).__init__()

        self.title(f'Enter Password ({self.site})')
        self.geometry('300x120')
        self.eval('tk::PlaceWindow . center')
        self.configure(background='#44F5E4')
        self.resizable(False, False)
        self.iconbitmap('Gui/fortnite.ico')
        self.attributes('-toolwindow', True)

        self.t_frame = tk.Frame(self, bg='#44F5E4', width=300, height=80)
        self.t_frame.pack(side=tk.TOP)

        self.b_frame = tk.Frame(self, bg='#44F5E4', width=300, height=60)
        self.b_frame.pack(side=tk.BOTTOM)

        self.l_frame = tk.Frame(self.t_frame, bg='#44F5E4', width=135, height=60)
        self.l_frame.pack(side=tk.LEFT)

        self.r_frame = tk.Frame(self.t_frame, bg='#44F5E4', width=135, height=40)
        self.r_frame.pack(side=tk.RIGHT)

        self.label = tk.Label(self.l_frame, text='Enter a password : ', bg='#44F5E4')
        self.label.place(width=120, height=30, x=5, y=16)

        self.enter = tk.Entry(self.r_frame, bd=1, relief=tk.SOLID, show='*')
        self.enter.place(width=120, height=30, x=5, y=5)

        self.button_close = tk.Button(self.b_frame, text='Close', relief=tk.SOLID, bd=1, command=self.close)
        self.button_close.place(width=50, height=20, y=35, x=185)

        self.button_ok = tk.Button(self.b_frame, text='Ok', relief=tk.SOLID, bd=1, command=self.ok)
        self.button_ok.place(width=50, height=20, y=35, x=240)

    def close(self):
        self.option = 0
        self.destroy()
        self.quit()

    def ok(self):
        self.password = self.enter.get()

        with open('pass.txt', 'r') as f:
            for line in f:
                password = hashlib.sha1(str(self.password).encode())

                if line == password.hexdigest():
                    self.option = 1

                else:
                    messagebox.showerror('Bad password', 'Unfortunately, the password is wrong !')

            self.destroy()
            self.quit()
