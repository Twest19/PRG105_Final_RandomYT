"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Tim West')

        self.label.pack()

        tkinter.mainloop()


my_gui = MyGUI2()

# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2
# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.first_label = tkinter.Label(self.top_frame, text='Tim West')
        self.second_label = tkinter.Label(self.top_frame, text='Undecided')

        self.third_label = tkinter.Label(self.bottom_frame, text='PRG - 105')

        self.first_label.pack(side='top')
        self.second_label.pack(side='top')
        self.third_label.pack(side='bottom')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


my_gui3 = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class JokeGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.joke_btn = tkinter.Button(self.main_window,
                                       text="What is cheese that doesn't belong to you called?",
                                       command=self.tell_joke)
        self.quit = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.joke_btn.pack()
        self.quit.pack()

        tkinter.mainloop()

    def tell_joke(self):
        tkinter.messagebox.showwarning('Jokester!', 'Nacho Cheese!')


my_joke = JokeGUI()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class InchCMConv:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("220x100")
        self.main_window.resizable(False, False)
        self.main_window.configure(bg='lightblue')

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Top Frame

        self.inch_label = tkinter.Label(self.top_frame, text="Enter inches here:", bg='lightblue')
        self.inch_entry = tkinter.Entry(self.top_frame, width=10)

        self.inch_label.pack(side='left')
        self.inch_entry.pack(side='left')

        # Mid Frame

        self.centimeters_label = tkinter.Label(self.mid_frame, text='Inch to CM:', bg='lightblue')
        self.entered = tkinter.StringVar()
        self.cm_label = tkinter.Label(self.mid_frame, textvariable=self.entered, bg='lightblue')

        self.centimeters_label.pack(side='left')
        self.cm_label.pack(side='left')

        # Bottom Frame

        self.conversion = tkinter.Button(self.bottom_frame, text='Convert',
                                         command=self.convert, bg='lightgreen')
        self.quit_btn = tkinter.Button(self.bottom_frame, text="Quit",
                                       command=self.main_window.destroy, bg='pink')

        self.conversion.pack(side='left')
        self.quit_btn.pack(side='left')

        # Frame pack

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        inch = float(self.inch_entry.get())
        cm = inch * 2.54

        self.entered.set(cm)


inch_converter = InchCMConv()
