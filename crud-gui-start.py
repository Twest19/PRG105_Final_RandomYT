import tkinter
import tkinter.messagebox
import pickle


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu,
                                        bg='lightgreen', padx=5, pady=5)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy,
                                          bg='pink', padx=5, pady=5)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = ChangeGUI(self.master)
        elif self.radio_var.get() == 4:
            _ = DeleteGUI(self.master)
        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')


class LookGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')
        self.look.geometry("320x100")

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=20)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search,
                                            bg='lightgreen', padx=5, pady=5)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back,
                                          bg='lightblue', padx=5, pady=5)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):  # goes back to main menu
        self.look.destroy()


class AddGUI:
    def __init__(self, master):
        self.master = master

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # Create New Window
        self.add = tkinter.Toplevel(master)
        self.add.title("Add Customer")
        self.add.geometry("250x100")

        # Create Frames for Add window
        self.top_frame = tkinter.Frame(self.add)
        self.mid_frame = tkinter.Frame(self.add)
        self.bot_frame = tkinter.Frame(self.add)

        # Top Frame
        self.name_value = tkinter.StringVar()
        self.name_label = tkinter.Label(self.top_frame, text="Enter a name:", padx=5)
        self.name_entry = tkinter.Entry(self.top_frame, width=20, textvariable=self.name_value)

        # Pack Top Frame
        self.name_label.pack(side='left')
        self.name_entry.pack(side='right')

        # Mid Frame
        self.email_value = tkinter.StringVar()
        self.email_label = tkinter.Label(self.mid_frame, text="Enter an email:", padx=5)
        self.email_entry = tkinter.Entry(self.mid_frame, width=20, textvariable=self.email_value)

        # Pack Mid
        self.email_label.pack(side='left')
        self.email_entry.pack(side='right')

        # Bottom Frame
        self.submit_btn = tkinter.Button(self.bot_frame, text="Add", command=self.save_data,
                                         bg='lightgreen', padx=5, pady=5)
        self.back_button = tkinter.Button(self.bot_frame, text='Main Menu', command=self.back,
                                          bg='lightblue', padx=5, pady=5)

        # Pack Bottom Frame Button
        self.submit_btn.pack(side='left')
        self.back_button.pack(side='left')

        # Pack Frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

    def save_data(self):  # save data when submit button is clicked
        name = self.name_entry.get()
        email = self.email_entry.get()

        # open the file, load to customers, close file. Do in each class
        if name in self.customers:
            tkinter.messagebox.showwarning('Error', 'That name already exist, try again!')
        else:
            self.customers[name] = email
            save_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, save_file)
            save_file.close()
            self.back()

    def back(self):  # goes back to main menu
        self.add.destroy()


class ChangeGUI:
    def __init__(self, master):
        self.master = master

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # Create New Window
        self.change = tkinter.Toplevel(master)
        self.change.title("Change Customer Email")
        self.change.geometry("450x100")

        # Create Frames for Add window
        self.top_frame = tkinter.Frame(self.change)
        self.mid_frame = tkinter.Frame(self.change)
        self.bot_frame = tkinter.Frame(self.change)

        # Top Frame
        self.change_value = tkinter.StringVar()
        self.change_label = tkinter.Label(self.top_frame, text='Enter the name of the customer you want to change:')
        self.name_entry = tkinter.Entry(self.top_frame, width=20, textvariable=self.change_value)

        # Pack Top Frame
        self.change_label.pack(side='left')
        self.name_entry.pack(side='right')

        # Mid Frame
        self.email_value = tkinter.StringVar()
        self.email_label = tkinter.Label(self.mid_frame, text="Now enter the new email:", padx=5)
        self.email_entry = tkinter.Entry(self.mid_frame, width=20, textvariable=self.email_value)

        # Pack Mid
        self.email_label.pack(side='left')
        self.email_entry.pack(side='right')

        # Bottom Frame
        self.submit_btn = tkinter.Button(self.bot_frame, text="Submit", command=self.save_data, bg='lightgreen')
        self.back_button = tkinter.Button(self.bot_frame, text='Main Menu', command=self.back, bg='lightblue')

        # Pack Bottom Frame Button
        self.submit_btn.pack(side='left')
        self.back_button.pack(side='left')

        # Pack Frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

    def save_data(self):  # save data when submit button is clicked
        name = self.name_entry.get()
        email = self.email_entry.get()

        if name not in self.customers:
            tkinter.messagebox.showwarning('Error', 'That name does not exist, try again!')
        else:
            self.customers[name] = email
            save_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, save_file)
            save_file.close()
            self.back()

    def back(self):  # goes back to main menu
        self.change.destroy()


class DeleteGUI:
    def __init__(self, master):
        self.master = master

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # Create New Window
        self.delete = tkinter.Toplevel(master)
        self.delete.geometry("450x100")
        self.delete.title("Delete Customer Email")

        # Create Frames for Add window
        self.top_frame = tkinter.Frame(self.delete)
        self.mid_frame = tkinter.Frame(self.delete)
        self.bot_frame = tkinter.Frame(self.delete)

        # Top Frame
        self.delete_label = tkinter.Label(self.top_frame, text='Enter the name of the customer you want to change:')
        self.delete_entry = tkinter.Entry(self.top_frame, width=20)

        # Pack Top Frame
        self.delete_label.pack(side='left')
        self.delete_entry.pack(side='right')

        # Mid Frame
        self.value = tkinter.StringVar()
        self.deleted_label = tkinter.Label(self.mid_frame, text="The following customer has been deleted: ", padx=5)
        self.delete_result = tkinter.Label(self.mid_frame, textvariable=self.value)

        # Pack Mid
        self.deleted_label.pack(side='left')
        self.delete_result.pack(side='right')

        # Bottom Frame
        self.delete_btn = tkinter.Button(self.bot_frame, text="Delete", command=self.delete_customer, bg='red')
        self.back_button = tkinter.Button(self.bot_frame, text='Main Menu', command=self.back, bg='lightblue')

        # Pack Bottom Frame Button
        self.delete_btn.pack(side='left')
        self.back_button.pack(side='right')

        # Pack Frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

    def delete_customer(self):  # save data when submit button is clicked
        name = self.delete_entry.get()

        if name in self.customers:
            self.value.set(f"{name}, {self.customers[name]}")

            del self.customers[name]
            save_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, save_file)
            save_file.close()
        else:
            tkinter.messagebox.showwarning('Error', 'That name does not exist, try again!')

    def back(self):  # goes back to main menu
        self.delete.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handles the remaining program logic
    _ = CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
