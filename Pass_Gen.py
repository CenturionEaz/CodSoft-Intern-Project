import tkinter as tk
import tkinter.messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Password Length
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.length_entry.insert(0, "12")  # Default length

        # Additional Text
        self.text_label = tk.Label(root, text="Additional Text:")
        self.text_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.text_entry = tk.Entry(root)
        self.text_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Character Sets
        self.upper_var = tk.BooleanVar()
        self.upper_check = tk.Checkbutton(root, text="Uppercase", variable=self.upper_var)
        self.upper_check.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.lower_var = tk.BooleanVar()
        self.lower_check = tk.Checkbutton(root, text="Lowercase", variable=self.lower_var)
        self.lower_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.digit_var = tk.BooleanVar()
        self.digit_check = tk.Checkbutton(root, text="Digits", variable=self.digit_var)
        self.digit_check.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.special_var = tk.BooleanVar()
        self.special_check = tk.Checkbutton(root, text="Special Characters", variable=self.special_var)
        self.special_check.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Password Display
        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = tk.Entry(root, width=50, state="readonly")
        self.password_entry.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        # Copy Button
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

    def generate_password(self):
        length = int(self.length_entry.get())
        additional_text = self.text_entry.get()
        use_upper = self.upper_var.get()
        use_lower = self.lower_var.get()
        use_digit = self.digit_var.get()
        use_special = self.special_var.get()

        chars = ""
        if use_upper:
            chars += string.ascii_uppercase
        if use_lower:
            chars += string.ascii_lowercase
        if use_digit:
            chars += string.digits
        if use_special:
            chars += string.punctuation

        if not chars:
            tk.messagebox.showwarning("Warning", "Please select at least one character set.")
            return

        password = additional_text + ''.join(random.choice(chars) for _ in range(length - len(additional_text)))
        password = ''.join(random.sample(password, len(password)))  # Shuffle the password
        self.password_entry.config(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state="readonly")

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            tk.messagebox.showinfo("Password Copied", "Password copied to clipboard.", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
    
