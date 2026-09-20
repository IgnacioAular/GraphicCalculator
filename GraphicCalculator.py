"""
Simple Calculator Application
Module: basic_tkinter_calculator
Purpose: A graphical user interface (GUI) calculator that performs 
         addition, subtraction, multiplication, and division
         using Python's Tkinter library.
Features: Input validation, error handling (invalid numbers, division by zero),
          clear function, and responsive layout.
"""

# ============= Import Required Libraries =============
# tkinter: Standard Python GUI toolkit for creating graphical interfaces
import tkinter as tk
# messagebox: Submodule from tkinter to display pop-up error/information windows
from tkinter import messagebox


# ============= Input Validation Function =============
def read_number(value):
    """
    Convert input value to a floating-point number.
    
    Args:
        value (str): The text input retrieved from an entry field
        
    Returns:
        float: Successfully converted number if input is valid
        None: If conversion fails (non-numeric input)
    """
    try:
        # Attempt to convert string input to float
        return float(value)
    except ValueError:
        # Return None if input cannot be converted to a number
        return None


# ============= Mathematical Operation Functions =============
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def sub(a, b):
    """Return the difference between two numbers (a minus b)."""
    return a - b

def mul(a, b):
    """Return the product of two numbers."""
    return a * b

def div(a, b):
    """
    Return the quotient of two numbers.
    
    Args:
        a (float): Dividend
        b (float): Divisor
        
    Returns:
        float: Result of division
        str: Error message if attempting to divide by zero
    """
    try:
        return a / b
    except ZeroDivisionError:
        # Handle mathematical error when dividing by zero
        return 'Cannot divide by zero.'


# ============= Core Calculator Logic =============
def calculator(operation):
    """
    Main handler for performing the selected calculation.
    
    Retrieves input values, validates data, runs the specified operation,
    and updates the result display. Shows error message for invalid inputs.
    
    Args:
        operation (str): Operation identifier; valid values:
                         'add', 'sub', 'mul', 'div'
    """
    # Get and convert both input values
    x = read_number(entry1.get())
    y = read_number(entry2.get())
    
    # Validate inputs: stop and show error if either value is invalid
    if x is None or y is None:
        messagebox.showerror('Error', 'Enter a valid number.')
        return None
    
    # Select and execute the mathematical operation
    match operation:
        case 'add':
            result = add(x, y)
        case 'sub':
            result = sub(x, y)
        case 'mul':
            result = mul(x, y)
        case 'div':
            result = div(x, y)
    
    # Update the display to show the calculation result
    show_result.set(f'Result: {result}')


# ============= Reset Function =============
def clear_entries():
    """
    Clear all input fields and the result display.
    
    Resets both entry boxes to empty and removes any displayed result.
    """
    # Delete all text from first input box
    entry1.delete(0, tk.END)
    # Delete all text from second input box
    entry2.delete(0, tk.END)
    # Clear the result text variable
    show_result.set('')


# ============= GUI Window Initialization =============
# Create the main application window
window = tk.Tk()
# Set title displayed in window title bar
window.title('Calculator')
# Define fixed window dimensions: width x height in pixels
window.geometry('250x250')
# Prevent user from resizing the window horizontally or vertically
window.resizable(False, False)

# Configure column layout weights for responsive resizing
# Column 0 gets proportion 1 of available space
window.columnconfigure(0, weight=1)
# Column 1 gets proportion 2 of available space
window.columnconfigure(1, weight=2)


# ============= Input Field Widgets =============
# Label for first number input
lb1 = tk.Label(window, text='Number 1:')
# Place label in grid: row 0, column 0, with padding, aligned to right
lb1.grid(row=0, column=0, padx=10, pady=10, sticky='e')
# Text entry box for first number
entry1 = tk.Entry(window)
# Place entry box in grid, aligned to left
entry1.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Label for second number input
lb2 = tk.Label(window, text='Number 2:')
lb2.grid(row=1, column=0, padx=10, pady=10, sticky='e')
# Text entry box for second number
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=10, sticky='w')


# ============= Button Container Frame =============
# Create frame to group operation buttons visually
frame_buttons = tk.Frame(window)
# Span frame across both columns
frame_buttons.grid(row=2, column=0, padx=20, pady=10, columnspan=2)


# ============= Operation Buttons =============
# Addition button: calls calculator with 'add' when clicked
btnAdd = tk.Button(frame_buttons, text='Add', width=10, 
                    command=lambda:calculator('add'))
btnAdd.grid(row=0, column=0, padx=5, pady=5)

# Subtraction button
btnSub = tk.Button(frame_buttons, text='Sub', width=10, 
                    command=lambda:calculator('sub'))
btnSub.grid(row=0, column=1, padx=5, pady=5)

# Multiplication button
btnMul = tk.Button(frame_buttons, text='Mul', width=10, 
                    command=lambda:calculator('mul'))
btnMul.grid(row=1, column=0, padx=5, pady=5)

# Division button
btnDiv = tk.Button(frame_buttons, text='Div', width=10, 
                    command=lambda:calculator('div'))
btnDiv.grid(row=1, column=1, padx=5, pady=5)

# Clear/Reset button
btnClear = tk.Button(frame_buttons, text='Clear', width=10, command=clear_entries)
btnClear.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


# ============= Result Display =============
# String variable to dynamically update result text
show_result = tk.StringVar()
# Label bound to the string variable; updates automatically when value changes
lbResult = tk.Label(window, textvariable=show_result, fg='blue', font=('Arial', 10))
lbResult.grid(row=3, column=0, columnspan=2, pady=10)


# ============= Run Application =============
# Start the Tkinter event loop — keeps window open and listens for user actions
window.mainloop()
