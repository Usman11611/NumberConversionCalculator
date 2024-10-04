# ----------------------------------------------
# Importing Required Modules
# ----------------------------------------------
from tkinter import *  # Importing all necessary components from the tkinter module
from tkinter import messagebox  # Importing the messagebox module for displaying pop-up messages
from tkinter import font  # Importing the font module for custom fonts

# ----------------------------------------------
# Main Application Window Setup
# ----------------------------------------------
root = Tk()  # Creating the main window for the application
root.title('Multi-Format Number Converter')  # Setting the title of the main window
root.geometry('800x700')  # Setting the dimensions of the window
root.configure(bg='#1e3c72')  # Setting the background color to a modern blue gradient-like shade

# ----------------------------------------------
# Variables Declaration
# ----------------------------------------------
num_input = StringVar()  # Variable to store the user's number input
format_input = StringVar(value='decimal')  # Variable to store the selected number format, default is 'decimal'
binary_val = StringVar()  # Variable to store the converted binary value
decimal_val = StringVar()  # Variable to store the converted decimal value
hex_val = StringVar()  # Variable to store the converted hexadecimal value
octal_val = StringVar()  # Variable to store the converted octal value
theme = StringVar(value='light')  # Variable to store the current theme, default is 'light'

# ----------------------------------------------
# Functions Definitions
# ----------------------------------------------

# Function to handle number conversion
def convert():
    steps_display.config(state=NORMAL)  # Enable editing to update the steps
    steps_display.delete(1.0, END)  # Clear the steps display before showing new steps
    try:
        input_value = num_input.get().strip()  # Get the input value from the user and strip any extra spaces
        input_format = format_input.get()  # Get the selected input format from the user
        
        if not input_value:  # Check if the input is empty
            raise ValueError("You must enter a number to convert.")  # Raise an error if no input is provided

        # Show the initial input and format
        steps_display.insert(END, f"Input: {input_value} ({input_format.capitalize()})\n\n")

        # Convert the input based on the selected format
        if input_format == 'decimal':  # If the format is decimal
            decimal_value = int(input_value)  # Convert input to integer directly
            steps_display.insert(END, f"Decimal to Decimal Conversion:\n")
            steps_display.insert(END, f"Input is already in decimal: {decimal_value}\n\n")
        elif input_format == 'binary':  # If the format is binary
            decimal_value = int(input_value, 2)  # Convert binary input to decimal
            steps_display.insert(END, f"Binary to Decimal Conversion:\n")
            for i, digit in enumerate(reversed(input_value)):
                steps_display.insert(END, f"{digit} * 2^{i} = {int(digit) * (2 ** i)}\n")
            steps_display.insert(END, f"Summing these values gives the decimal value: {decimal_value}\n\n")
        elif input_format == 'octal':  # If the format is octal
            decimal_value = int(input_value, 8)  # Convert octal input to decimal
            steps_display.insert(END, f"Octal to Decimal Conversion:\n")
            for i, digit in enumerate(reversed(input_value)):
                steps_display.insert(END, f"{digit} * 8^{i} = {int(digit) * (8 ** i)}\n")
            steps_display.insert(END, f"Summing these values gives the decimal value: {decimal_value}\n\n")
        elif input_format == 'hexadecimal':  # If the format is hexadecimal
            decimal_value = int(input_value, 16)  # Convert hexadecimal input to decimal
            steps_display.insert(END, f"Hexadecimal to Decimal Conversion:\n")
            for i, digit in enumerate(reversed(input_value)):
                steps_display.insert(END, f"{digit.upper()} * 16^{i} = {int(digit, 16) * (16 ** i)}\n")
            steps_display.insert(END, f"Summing these values gives the decimal value: {decimal_value}\n\n")
        else:
            raise ValueError("Invalid input format selected.")  # Raise an error if an invalid format is selected

        # Update the output fields with the converted values
        binary_value = bin(decimal_value)[2:]
        binary_val.set(f"{binary_value} (Binary)")
        steps_display.insert(END, f"Decimal to Binary Conversion:\n")
        steps_display.insert(END, f"Starting with {decimal_value}, divide by 2 and keep track of the remainders:\n")
        temp_value = decimal_value
        binary_steps = []
        while temp_value > 0:
            binary_steps.append(temp_value % 2)
            steps_display.insert(END, f"{temp_value} ÷ 2 = {temp_value // 2}, remainder: {temp_value % 2}\n")
            temp_value //= 2
        steps_display.insert(END, f"Binary value (bottom to top of remainders): {binary_value}\n\n")
        
        decimal_val.set(f"{decimal_value} (Decimal)")  # Update the decimal value field

        hex_value = hex(decimal_value)[2:].upper()
        hex_val.set(f"{hex_value} (Hexadecimal)")
        steps_display.insert(END, f"Decimal to Hexadecimal Conversion:\n")
        steps_display.insert(END, f"Starting with {decimal_value}, divide by 16 and keep track of the remainders:\n")
        temp_value = decimal_value
        hex_steps = []
        while temp_value > 0:
            remainder = temp_value % 16
            hex_digit = hex(remainder)[2:].upper()
            hex_steps.append(hex_digit)
            steps_display.insert(END, f"{temp_value} ÷ 16 = {temp_value // 16}, remainder: {hex_digit}\n")
            temp_value //= 16
        steps_display.insert(END, f"Hexadecimal value (bottom to top of remainders): {hex_value}\n\n")
        
        octal_value = oct(decimal_value)[2:]
        octal_val.set(f"{octal_value} (Octal)")
        steps_display.insert(END, f"Decimal to Octal Conversion:\n")
        steps_display.insert(END, f"Starting with {decimal_value}, divide by 8 and keep track of the remainders:\n")
        temp_value = decimal_value
        octal_steps = []
        while temp_value > 0:
            octal_steps.append(temp_value % 8)
            steps_display.insert(END, f"{temp_value} ÷ 8 = {temp_value // 8}, remainder: {temp_value % 8}\n")
            temp_value //= 8
        steps_display.insert(END, f"Octal value (bottom to top of remainders): {octal_value}\n\n")

    except ValueError as e:  # Catch any value errors that occur during conversion
        messagebox.showerror('Error', str(e))  # Display an error message if something goes wrong
    
    steps_display.config(state=DISABLED)  # Disable editing after updating the steps

# Function to clear all input and output fields
def clear():
    num_input.set('')  # Clear the user input field
    binary_val.set('')  # Clear the binary output field
    decimal_val.set('')  # Clear the decimal output field
    hex_val.set('')  # Clear the hexadecimal output field
    octal_val.set('')  # Clear the octal output field
    steps_display.config(state=NORMAL)  # Enable editing to clear the steps display
    steps_display.delete(1.0, END)  # Clear the steps display
    steps_display.config(state=DISABLED)  # Disable editing after clearing the steps

# Function to exit the application
def exit_program():
    if messagebox.askyesno('Exit', 'Do you really want to Exit?'):  # Ask the user for confirmation to exit
        root.destroy()  # Close the application window if the user confirms

# Function to toggle between light and dark themes
def toggle_theme():
    if theme.get() == 'light':  # Check if the current theme is light
        root.configure(bg='#263238')  # Change the background color to a dark shade
        title.configure(bg='#37474F', fg='white')  # Update the title's background and text color to match the dark theme
        for widget in root.winfo_children():  # Loop through all child widgets in the root window
            if isinstance(widget, Label) or isinstance(widget, Radiobutton):  # Check if the widget is a label or radio button
                widget.configure(bg='#263238', fg='white', selectcolor='#37474F')  # Apply dark theme to labels and radio buttons
            if isinstance(widget, Entry):  # Check if the widget is an entry field
                widget.configure(bg='#546E7A', fg='white', insertbackground='white')  # Apply dark theme to entry fields
        theme.set('dark')  # Set the theme variable to dark
        toggle_button.configure(text='Light Mode')  # Update the button text to 'Light Mode'
    else:
        root.configure(bg='#1e3c72')  # Change the background color to the modern blue shade
        title.configure(bg='#0288D1', fg='white')  # Update the title's background and text color to match the light theme
        for widget in root.winfo_children():  # Loop through all child widgets in the root window
            if isinstance(widget, Label) or isinstance(widget, Radiobutton):  # Check if the widget is a label or radio button
                widget.configure(bg='#e0f7fa', fg='black', selectcolor='#e0f7fa')  # Apply light theme to labels and radio buttons
            if isinstance(widget, Entry):  # Check if the widget is an entry field
                widget.configure(bg='white', fg='black', insertbackground='black')  # Apply light theme to entry fields
        theme.set('light')  # Set the theme variable to light
        toggle_button.configure(text='Dark Mode')  # Update the button text to 'Dark Mode'

# Create the Toggle Theme Button globally so it can be referenced inside the function
toggle_button = Button(root, text='Dark Mode', font=('Arial', 16), fg='white', bg='#00796B', activebackground='#00796B', activeforeground='white', width=12, relief=RAISED, bd=5, command=toggle_theme)
toggle_button.place(x=450, y=550)  # Position the toggle theme button on the window

# ----------------------------------------------
# UI Elements: Title and Input Fields
# ----------------------------------------------

# Title Label with a modern font and shadow effect
title_font = font.Font(family='Helvetica', size=28, weight='bold')
title = Label(root, text='Multi-Format Number Converter', font=title_font, bg='#0288D1', fg='white', relief=RAISED, padx=10, pady=10)
title.pack(pady=10)  # Pack the title label into the window with padding

# Input Label and Entry Field
input_label = Label(root, text='Enter a Number:', font=('Arial', 16), bg='#1e3c72', fg='white')  # Label for the input field
input_label.place(x=50, y=100)  # Position the input label on the window
input_entry = Entry(root, font=('Arial', 16), textvariable=num_input, justify=CENTER, relief=SOLID, bd=2, width=25)  # Entry field for the number input
input_entry.place(x=250, y=100)  # Position the input entry field on the window

# ----------------------------------------------
# UI Elements: Radio Buttons for Input Format
# ----------------------------------------------

# Format Selection Label
format_label = Label(root, text='Select Input Format:', font=('Arial', 16), bg='#1e3c72', fg='white')  # Label for the format selection
format_label.place(x=50, y=150)  # Position the format selection label on the window

# Radio Buttons for Each Format
formats = ['decimal', 'binary', 'octal', 'hexadecimal']  # List of formats
x_positions = [250, 350, 450, 550]  # X positions for the radio buttons

# Loop to create radio buttons for each format
for i, fmt in enumerate(formats):
    Radiobutton(root, text=fmt.capitalize(), variable=format_input, value=fmt, font=('Arial', 14), bg='#1e3c72', fg='white', selectcolor='#37474F').place(x=x_positions[i], y=150)

# ----------------------------------------------
# UI Elements: Output Fields for Converted Values
# ----------------------------------------------

# Binary Output Label and Entry Field
binary_label = Label(root, text='Binary:', font=('Arial', 16), bg='#1e3c72', fg='white')  # Label for the binary output
binary_label.place(x=50, y=200)  # Position the binary label on the window
binary_entry = Entry(root, font=('Arial', 16), textvariable=binary_val, justify=CENTER, relief=SOLID, bd=2, width=25, state='readonly')  # Entry field for the binary output (read-only)
binary_entry.place(x=250, y=200)  # Position the binary entry field on the window

# Decimal Output Label and Entry Field
decimal_label = Label(root, text='Decimal:', font=('Arial', 16), bg='#1e3c72', fg='white')  # Label for the decimal output
decimal_label.place(x=50, y=250)  # Position the decimal label on the window
decimal_entry = Entry(root, font=('Arial', 16), textvariable=decimal_val, justify=CENTER, relief=SOLID, bd=2, width=25, state='readonly')  # Entry field for the decimal output (read-only)
decimal_entry.place(x=250, y=250)  # Position the decimal entry field on the window

# Hexadecimal Output Label and Entry Field
hex_label = Label(root, text='Hexadecimal:', font=('Arial', 16), bg='#1e3c72', fg='white')  # Label for the hexadecimal output
hex_label.place(x=50, y=300)  # Position the hexadecimal label on the window
hex_entry = Entry(root, font=('Arial', 16), textvariable=hex_val, justify=CENTER, relief=SOLID, bd=2, width=25, state='readonly')  # Entry field for the hexadecimal output (read-only)
hex_entry.place(x=250, y=300)  # Position the hexadecimal entry field on the window

# Octal Output Label and Entry Field
octal_label = Label(root, text='Octal:', font=('Arial', 16), bg='#1e3c72', fg='white')  # Label for the octal output
octal_label.place(x=50, y=350)  # Position the octal label on the window
octal_entry = Entry(root, font=('Arial', 16), textvariable=octal_val, justify=CENTER, relief=SOLID, bd=2, width=25, state='readonly')  # Entry field for the octal output (read-only)
octal_entry.place(x=250, y=350)  # Position the octal entry field on the window

# ----------------------------------------------
# UI Elements: Steps Display
# ----------------------------------------------

root.geometry('800x700')  # Set the new window size

# Steps Display Label
steps_label = Label(root, text='Conversion Steps:', font=('Arial', 16), bg='#1e3c72', fg='white')
steps_label.place(x=50, y=400)

# Steps Display Text Widget (read-only)
steps_display = Text(root, font=('Arial', 12), height=8, width=70, relief=SOLID, bd=2, state=DISABLED)
steps_display.place(x=50, y=430)  # Adjust Y-coordinate here


# ----------------------------------------------
# UI Elements: Buttons for Actions
# ----------------------------------------------

# Adjust buttons for better alignment and spacing
button_frame = Frame(root, bg='#1e3c72')
button_frame.place(x=200, y=550)

# Convert Button
convert_button = Button(button_frame, text='Convert', font=('Arial', 16), fg='white', bg='#0288D1', activebackground='#0288D1', activeforeground='white', width=10, relief=RAISED, bd=5, command=convert)
convert_button.grid(row=0, column=0, padx=10)

# Clear Button
clear_button = Button(button_frame, text='Clear', font=('Arial', 16), fg='white', bg='#FF5722', activebackground='#FF5722', activeforeground='white', width=10, relief=RAISED, bd=5, command=clear)
clear_button.grid(row=0, column=1, padx=10)

# Exit Button
exit_button = Button(button_frame, text='Exit', font=('Arial', 16), fg='white', bg='#F44336', activebackground='#F44336', activeforeground='white', width=10, relief=RAISED, bd=5, command=exit_program)
exit_button.grid(row=0, column=2, padx=10)

# ----------------------------------------------
# Running the Main Application Loop
# ----------------------------------------------
root.mainloop()  # Start the Tkinter event loop