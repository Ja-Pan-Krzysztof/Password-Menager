import tkinter as tk


class AddPassword(tk.Tk):
    def __init__(self):
        self.password = None
        self.site = None
        super(AddPassword, self).__init__()

        self.title('Create New Password')
        self.geometry('300x120-2300+200')
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

        self.label1 = tk.Label(self.l_frame, text='Enter a site : ', bg='pink')
        self.label1.place(width=120, height=30, x=5, y=5)
        self.label2 = tk.Label(self.l_frame, text='Enter a password', bg='pink')
        self.label2.place(width=120, height=30, x=5, y=52)

        self.enter1 = tk.Entry(self.r_frame, bd=1, relief=tk.SOLID)
        self.enter1.place(width=120, height=30, x=5, y=5)
        self.enter2 = tk.Entry(self.r_frame, bd=1, relief=tk.SOLID, show='*')
        self.enter2.place(width=120, height=30, x=5, y=50)

        self.button_close = tk.Button(self.b_frame, text='Close', relief=tk.SOLID, bd=1, command=self.close)
        self.button_close.place(width=50, height=20, y=5, x=185)

        self.button_ok = tk.Button(self.b_frame, text='Ok', relief=tk.SOLID, bd=1, command=self.ok)
        self.button_ok.place(width=50, height=20, y=5, x=240)

    def close(self):
        self.destroy()
        self.quit()

    def ok(self):
        self.site = self.enter1.get()
        self.password = self.enter2.get()

        self.destroy()
        self.quit()
