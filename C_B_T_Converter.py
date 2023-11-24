import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Function to execute a file
def execute_file(file_name):
    subprocess.run(["python", file_name])

# Function triggered by button click
def on_button_click(i):
    execute_file(files[i])

# List of files
files = ['Currency Converter', 'Base Converter ', 'Time Zone']

# Create the main Tkinter window
root = tk.Tk()
root.title("Choose a file to execute")
root.configure(bg='#000000')  # Set background color

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = screen_height // 3
    window.geometry(f'{width}x{height}+{x}+{y}')

# Define colors
button_bg_color = '#FFFFFF'  # Button background color
button_fg_color = '#000000'  # Button text color

# Create buttons for each file
for i, file in enumerate(files):
    button = tk.Button(root, text=file, command=lambda i=i: on_button_click(i), bg=button_bg_color, fg=button_fg_color)
    button.config(font=('Arial', 12), padx=10, pady=5)  # Set font, padding
    button.pack(padx=20, pady=5, fill=tk.X)  # Add padding and fill in X direction
    button.bind("<Enter>", lambda e, button=button: button.config(bg='#808080'))  # Hover color
    button.bind("<Leave>", lambda e, button=button: button.config(bg=button_bg_color))  # Restore original color

# Calculate window width and height based on button layout
width = max(button.winfo_reqwidth() for button in root.winfo_children()) + 40
height = len(files) * 50 + 40  # Adjust height based on number of buttons

# Increase width and height by 5%
width *= 1.8
height *= .9

# Run the Tkinter main loop
root.update_idletasks()
center_window(root, int(width), int(height))
root.mainloop()
