import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="Witaj świecie!")
        self.label2 = tkinter.Label(self.top_frame, text="To jest program z GUI.")
        self.label3 = tkinter.Label(self.top_frame, text="Programowanie z Pythonem.")

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.bottom_frame, text="Witaj świecie!")
        self.label5 = tkinter.Label(self.bottom_frame, text="To jest program z GUI.")
        self.label6 = tkinter.Label(self.bottom_frame, text="Programowanie z Pythonem.")

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


my_gui = MyGui()