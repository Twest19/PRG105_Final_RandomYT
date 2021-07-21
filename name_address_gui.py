import tkinter


class NameAddress:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("300x120")
        self.main_window.title("Info Shower")

        # Create frames

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create stringvar
        self.name = tkinter.StringVar()
        self.street = tkinter.StringVar()
        self.city = tkinter.StringVar()

        # Top Frame

        self.name_label = tkinter.Label(self.top_frame, textvariable=self.name)
        self.street_label = tkinter.Label(self.top_frame, textvariable=self.street)
        self.city_label = tkinter.Label(self.top_frame, textvariable=self.city)

        # Pack labels

        self.name_label.pack()
        self.street_label.pack()
        self.city_label.pack()

        # Bottom Frame
        self.info_btn = tkinter.Button(self.bottom_frame, text='Show Info', command=self.show_info)
        self.quit_btn = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy, bg='pink')

        # Pack Bottom Buttons

        self.info_btn.pack(side='left')
        self.quit_btn.pack(side='right')

        # Pack Frames

        self.top_frame.pack()
        self.bottom_frame.pack()

        # Call mainloop

        tkinter.mainloop()

    def show_info(self):
        self.name.set("Tim West")
        self.street.set("1600 Pennsylvania Avenue NW,")
        self.city.set("Washington, DC 20500")


my_info = NameAddress()
