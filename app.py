from tkinter import *
import math
from tkinter import font as tkfont

root = Tk()

# for calculations
def click(event):
    global scValue
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(scValue.get())
        except Exception:
            value = "Error"
        scValue.set(value)
        screen.update()
    elif text == "C":
        scValue.set("")
        screen.update()
    else:
        scValue.set(scValue.get() + text)
        screen.update()

# Additional functions for advanced operations
def sqrt_func():
    try:
        value = math.sqrt(float(scValue.get()))
        scValue.set(value)
    except Exception:
        scValue.set("Error")
    screen.update()

def square_func():
    try:
        value = float(scValue.get()) ** 2
        scValue.set(value)
    except Exception:
        scValue.set("Error")
    screen.update()

def backspace():
    current = scValue.get()
    scValue.set(current[:-1])
    screen.update()

# GUI frame size
root.geometry("500x700")
# GUI title
root.title("Enhanced Calculator")
# GUI icon
try:
    root.wm_iconbitmap("1.ico")
except:
    pass  # Icon file might not exist
# GUI background
root.config(bg="#2c3e50")  # Dark blue background

# Define custom fonts
title_font = tkfont.Font(family="Helvetica", size=22, weight="bold")
author_font = tkfont.Font(family="Helvetica", size=12, slant="italic")
display_font = tkfont.Font(family="Consolas", size=40, weight="bold")

# Upper frame and label
f1 = Frame(root, bg="#3498db", borderwidth=0, relief=FLAT)
Label(f1, text="Modern Calculator", font=title_font, bg="#3498db", fg="white").pack(pady=10)
Label(f1, text="-by Uttam", font=author_font, bg="#3498db", fg="white").pack(side=RIGHT, anchor=SE, padx=10, pady=5)
f1.pack(side=TOP, fill=X)

# Entry value
scValue = StringVar()
scValue.set("")
screen_frame = Frame(root, bg="#34495e", padx=10, pady=10)
screen = Entry(screen_frame, textvar=scValue, font=display_font, relief=FLAT, bg="#ecf0f1", fg="#2c3e50", justify=RIGHT, bd=0)
screen.pack(fill=X, ipady=15)
screen_frame.pack(fill=X, padx=20, pady=20)

# Define button fonts and styles
button_font = tkfont.Font(family="Helvetica", size=18, weight="bold")

# Button colors
num_color = "#ecf0f1"  # Light gray for numbers
op_color = "#e74c3c"   # Red for operations
func_color = "#2ecc71"  # Green for functions
clear_color = "#f39c12"  # Orange for clear/backspace
equal_color = "#3498db"  # Blue for equals

# Button hover effect
def on_enter(e):
    e.widget['background'] = '#7f8c8d'  # Darker gray on hover

def on_leave(e, original_color):
    e.widget['background'] = original_color

# Buttons frame with standard grid layout
button_layout = [
    ['7', '8', '9', '/', '√'],
    ['4', '5', '6', '*', 'x²'],
    ['1', '2', '3', '-', 'C'],
    ['0', '.', '=', '+', '⌫']
]

# Main buttons container
buttons_frame = Frame(root, bg="#2c3e50", padx=20, pady=10)
buttons_frame.pack(fill=BOTH, expand=True)

# Create buttons using the layout
for i, row in enumerate(button_layout):
    buttons_frame.grid_rowconfigure(i, weight=1)
    for j, char in enumerate(button_layout[i]):
        buttons_frame.grid_columnconfigure(j, weight=1)

        # Set button properties based on type
        if char.isdigit() or char == '.':
            bg_color = num_color
        elif char in '+-*/':
            bg_color = op_color
        elif char in ['√', 'x²']:
            bg_color = func_color
        elif char in ['C', '⌫']:
            bg_color = clear_color
        elif char == '=':
            bg_color = equal_color
        else:
            bg_color = num_color

        # Create the button with rounded corners and modern styling
        b = Button(buttons_frame, text=char, font=button_font, bg=bg_color, fg="#2c3e50",
                  relief=FLAT, borderwidth=0, padx=10, pady=15)

        # Add hover effects
        b.bind("<Enter>", on_enter)
        b.bind("<Leave>", lambda e, color=bg_color: on_leave(e, color))

        # Bind functions
        if char == '√':
            b.bind("<Button-1>", lambda _: sqrt_func())
        elif char == 'x²':
            b.bind("<Button-1>", lambda _: square_func())
        elif char == '⌫':
            b.bind("<Button-1>", lambda _: backspace())
        else:
            b.bind("<Button-1>", click)

        # Place button in grid with padding
        b.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

# Bottom frame for additional information
fl = Frame(root, bg="#3498db", borderwidth=0, relief=FLAT)
Label(fl, text="Thanks for using me!", font=title_font, bg="#3498db", fg="white").pack(pady=10)
fl.pack(side=BOTTOM, fill=X)

# Support for keyboard input
def key_pressed(event):
    key = event.char
    if key.isdigit() or key in "+-*/.%":
        scValue.set(scValue.get() + key)
    elif key == '\r':  # Enter key for "="
        click(event)
    elif key == '\x08':  # Backspace key
        backspace()

root.bind("<Key>", key_pressed)

root.mainloop()
