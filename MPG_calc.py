"""
Write a GUI program that calculates a car’s gas mileage. The program’s window should have Entry widgets that let
the user enter the number of gallons of gas the car holds, and the number of miles it can be driven on a full tank.
When a Calculate MPG button is clicked, the program should display the number of miles that the car may be driven per
gallon of gas. Use the following formula to calculate miles per gallon:
"""
import tkinter


class MpgCalc:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("400x150")
        self.main_window.title("MPG Calculator")

        # Create Frames

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)
        self.conv_frame = tkinter.Frame(self.main_window)

        # Create IntVar
        self.converted_val = tkinter.IntVar()

        # Top Frame
        self.gallon_label = tkinter.Label(self.top_frame, text="Enter how many gallons your car holds:")
        self.gallon_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack Top Frame Buttons/Label
        self.gallon_label.grid(row=0, column=0)
        self.gallon_entry.grid(row=1, column=0)

        # Mid Frame
        self.miles_label = tkinter.Label(self.mid_frame, text="Enter how many miles you have drove:")
        self.miles_entry = tkinter.Entry(self.mid_frame, width=10)

        # Pack Mid Buttons\labels
        self.miles_label.pack()
        self.miles_entry.pack()

        # Bottom Frame

        self.miles_label = tkinter.Label(self.bot_frame, text="Convert to miles per gallons:")
        self.outcome = tkinter.Label(self.bot_frame, textvariable=self.converted_val)

        # Pack Bottom Button/Labels

        self.miles_label.grid(row=2, column=0)
        self.outcome.grid(row=2, column=1)

        # Conversion Frame
        try:
            self.convert_btn = tkinter.Button(self.conv_frame, text='Convert', command=self.converter, bg='lightgreen')
        except ValueError:
            pass
        else:
            self.quit_btn = tkinter.Button(self.conv_frame, text="Quit",
                                           command=self.main_window.destroy, bg='pink')

        # Pack Conversion row buttons

        self.convert_btn.grid(row=3, column=0)
        self.quit_btn.grid(row=3, column=1)

        # Pack Frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()
        self.conv_frame.pack()

        tkinter.mainloop()

    def converter(self):
        try:
            gallons = float(self.gallon_entry.get())
            miles = float(self.miles_entry.get())
            mpg = miles / gallons
        except ValueError:
            pass
        else:
            self.converted_val.set(f"{mpg:.2f}")


calc = MpgCalc()
