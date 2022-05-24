import tkinter as tk
from cryptography.fernet import Fernet
from functools import partial


class AppGui(tk.Tk):
    def __init__(self):
        super(AppGui, self).__init__()
        self.password_dict = {}
        self.key = 'HD_u6rEZu_3Ro-ntk2lz_V1oKmiAOEFZ3nxuRT6Uip0='
        self.password = 'Mnichuj'

        self.title('Password Menager')
        self.geometry('800x600-2000+50')
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

        self.pass_label = tk.Label(self.r_frame, text='Passwords')
        self.pass_label.place(height=25, width=290, x=5, y=5)

        with open('all.pass', 'r') as f:
            for line in f:
                site, password = line.split(':')
                self.password_dict[site] = password

        a = 45
        b = 0
        for key, value in self.password_dict.items():
            site = tk.Button(self.l_frame, text=f'{key}', relief=tk.RIDGE, command=partial(self.command_button, b))
            site.place(height=25, width=190, x=5, y=a)

            a += 27
            b += 1

    def command_button(self, pass_num):
        a = 0
        for key, value in self.password_dict.items():
            if a == pass_num:
                pass_gui = PassGui(key)
                pass_gui.mainloop()

                return [pass_num, self.show_passwords(pass_gui.password)]

            a += 1

    '''def show_passwords(self, passwords: list):
        num_pass = passwords[0]
        password = passwords[1]
        a = 45

        if password == self.password:
            with open('all.pass', 'r') as f:
                for line in f:
                    site, encrypted = line.split(':')
                    self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

            for key, value in self.password_dict.items():
                pas = tk.Label(self.r_frame, text=f'{value}', relief=tk.RIDGE)
                pas.place(height=25, width=290, x=5, y=a)

                a += 27

        else:
            print('False')'''


class PassGui(tk.Tk):
    def __init__(self, site: str):
        self.site = site
        self.option = 0
        self.password = None
        super(PassGui, self).__init__()

        self.title(f'Enter Password ({self.site})')
        self.geometry('300x120-2300+200')
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
        self.option = 1
        self.password = self.enter.get()
        self.destroy()
        self.quit()



        # relief - obramowania
