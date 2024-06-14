import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

# Function to generate a random password
def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number for password length.")
        return

    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    
    if length < 4:
        messagebox.showwarning("Warning", "Password length should be at least 4 characters for security.")
        return
    
    char_set = ""
    if include_uppercase:
        char_set += string.ascii_uppercase
    if include_lowercase:
        char_set += string.ascii_lowercase
    if include_numbers:
        char_set += string.digits
    if include_symbols:
        char_set += string.punctuation
    
    if not char_set:
        messagebox.showwarning("Warning", "You must select at least one character set!")
        return

    password = []
    
    # Ensure the password contains at least one of each selected character type
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_symbols:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password length with random choices from the selected character sets
    while len(password) < length:
        password.append(random.choice(char_set))
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string
    password = ''.join(password)
    
    password_var.set(password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Create the main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Create and place widgets
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Password length
length_var = tk.StringVar()
ttk.Label(main_frame, text="Password Length:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
length_entry = ttk.Entry(main_frame, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Options
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

ttk.Checkbutton(main_frame, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)
ttk.Checkbutton(main_frame, text="Include Lowercase Letters", variable=lowercase_var).grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)
ttk.Checkbutton(main_frame, text="Include Numbers", variable=numbers_var).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)
ttk.Checkbutton(main_frame, text="Include Symbols", variable=symbols_var).grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

# Generate password button
ttk.Button(main_frame, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Password display
password_var = tk.StringVar()
password_entry = ttk.Entry(main_frame, textvariable=password_var, width=40)
password_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

# Copy to clipboard button
ttk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
