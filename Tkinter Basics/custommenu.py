from tkinter import *
from tkinter.ttk import *

class Gui:

    def __init__(self):
        self.root = Tk()

        # Set up the Combobox
        self.selections = Combobox(self.root)
        self.selections['values'] = ['Apples', 'Oranges', 'Blueberries', 'Bananas', 'Custom']
        self.selections.pack()

        # The Entry to be shown if "Custom" is selected
        self.custom_field = Entry(self.root)
        self.show_custom_field = False

        # Check the selection in 100 ms
        self.root.after(100, self.check_for_selection)

    def check_for_selection(self):
        value = self.selections.get()

        # If the value is equal to "Custom" and show_field is set to False
        if value == 'Custom' and not self.show_custom_field:

            # Set show_field to True and pack() the custom entry field
            self.show_custom_field = True

            # Create a new window how we did when we made self.root
            self.new_window = Tk()

            # Create the Entry that will go in the window. The previous Entry widget from line 16, can be removed
            self.custom_field = Entry(self.new_window)
            self.custom_field.pack()

            # Run the new window like we did the original
            self.new_window.mainloop()


        # If the value DOESNT equal "Custom"
        elif value != 'Custom':

            # Destroy the new window that was created if it exists
            if self.show_custom_field:
                self.new_window.destroy()

            # Set show_field to False
            self.show_custom_field = False

        # If the value IS "Custom" and we're showing the custom_feild
        elif value == 'Custom' and self.show_custom_field:
            print('yes')


        # Call this method again to keep checking the selection box
        self.root.after(100, self.check_for_selection)


app = Gui()
app.root.mainloop()