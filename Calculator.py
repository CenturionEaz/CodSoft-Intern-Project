import tkinter as tk
from tkinter import colorchooser, font
from math import sqrt, sin, cos, tan, log, radians, degrees

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calculator")
        self.memory = 0  # Initialize memory variable

        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.create_buttons()
        self.create_expander()

        self.create_menu()

    def create_buttons(self):
        basic_buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('M+', 5, 0), ('MC', 5, 1), ('MR', 5, 2), ('C', 5, 3),
        ]

        for (text, row, col) in basic_buttons:
            btn = tk.Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.on_click(t))
            btn.grid(row=row, column=col)

    def create_expander(self):
        self.expanded = False
        self.expander_button = tk.Button(self.root, text="▼", command=self.toggle_expander)
        self.expander_button.grid(row=6, column=4)

    def toggle_expander(self):
        if self.expanded:
            self.hide_scientific_buttons()
            self.expander_button.config(text="▼")
        else:
            self.show_scientific_buttons()
            self.expander_button.config(text="▲")
        self.expanded = not self.expanded

    def show_scientific_buttons(self):
        scientific_buttons = [
            ('√', 6, 0), ('x^2', 6, 1), ('sin', 6, 2), ('cos', 6, 3),
            ('tan', 7, 0), ('log', 7, 1), ('π', 7, 2), ('deg', 7, 3)
        ]

        for (text, row, col) in scientific_buttons:
            btn = tk.Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.on_click(t))
            btn.grid(row=row, column=col)

    def hide_scientific_buttons(self):
        for widget in self.root.winfo_children():
            if widget.grid_info()['row'] >= 6:
                widget.grid_forget()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Change Number Color", command=self.change_number_color)
        file_menu.add_command(label="Change Screen Color", command=self.change_screen_color)
        file_menu.add_command(label="Change GUI Color", command=self.change_gui_color)
        file_menu.add_separator()
        file_menu.add_command(label="Increase Window Size", command=self.increase_window_size)
        file_menu.add_command(label="Increase Font Size", command=self.increase_font_size)
        file_menu.add_command(label="Increase Output Screen Size", command=self.increase_output_size)

        menu_bar.add_cascade(label="File", menu=file_menu)

        self.root.config(menu=menu_bar)

    def change_number_color(self):
        color = colorchooser.askcolor(title="Choose Number Color")
        if color[1]:
            self.entry.config(fg=color[1])

    def change_screen_color(self):
        color = colorchooser.askcolor(title="Choose Screen Color")
        if color[1]:
            self.entry.config(bg=color[1])

    def change_gui_color(self):
        color = colorchooser.askcolor(title="Choose GUI Color")
        if color[1]:
            self.root.config(bg=color[1])

    def increase_window_size(self):
        self.root.geometry("600x400")

    def increase_font_size(self):
        current_font = font.Font(font=self.entry['font'])
        current_font.configure(size=current_font.cget('size') + 2)
        self.entry.config(font=current_font)

    def increase_output_size(self):
        self.entry.config(width=50)

    def on_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        elif text == 'M+':
            self.memory_add()
        elif text == 'MC':
            self.memory_clear()
        elif text == 'MR':
            self.memory_recall()
        elif text == '√':
            self.square_root()
        elif text == 'x^2':
            self.square()
        elif text in ('sin', 'cos', 'tan', 'log'):
            self.trig_log(text)
        else:
            self.entry.insert(tk.END, text)

    def memory_add(self):
        try:
            self.memory += float(self.entry.get())
        except:
            self.memory = float(self.entry.get()) if self.entry.get() != '' else 0

    def memory_clear(self):
        self.memory = 0

    def memory_recall(self):
        self.entry.insert(tk.END, str(self.memory))

    def square_root(self):
        try:
            result = sqrt(float(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def square(self):
        try:
            result = float(self.entry.get()) ** 2
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def trig_log(self, func):
        try:
            num = float(self.entry.get())
            if func == 'sin':
                result = sin(num)
            elif func == 'cos':
                result = cos(num)
            elif func == 'tan':
                result = tan(num)
            elif func == 'log':
                result = log(num)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
