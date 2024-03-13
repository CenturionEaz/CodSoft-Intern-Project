import tkinter as tk
from tkinter import messagebox, simpledialog, colorchooser

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Menu Bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Change GUI Color", command=self.change_gui_color)
        self.file_menu.add_command(label="Change Button Color", command=self.change_button_color)
        self.file_menu.add_command(label="Change Text Color", command=self.change_text_color)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", bg="green", fg="red", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # Task Entry
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Add Task Button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=2, padx=10, pady=10)

        # Task List
        self.task_list = tk.Listbox(root, width=50)
        self.task_list.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.task_list.bind("<Double-Button-1>", self.edit_task)

        # Button Frame
        self.button_frame = tk.Frame(root)
        self.button_frame.grid(row=3, column=0, columnspan=3)

        # Delete Task Button
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=0, padx=5, pady=10)

        # Edit Task Button
        self.edit_button = tk.Button(self.button_frame, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=0, column=1, padx=5, pady=10)

        # Mark as Complete Button
        self.complete_button = tk.Button(self.button_frame, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.grid(row=0, column=2, padx=5, pady=10)

        # Default text color
        self.default_text_color = "black"
        self.complete_task_color = self.default_text_color
        self.incomplete_task_color = self.default_text_color

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append((task, False))  # Tuple (task, completion status)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            confirmed = messagebox.askyesno("Confirm", "Are you sure you want to delete this task?")
            if confirmed:
                del self.tasks[selected_task_index[0]]
                self.update_task_list()
                self.save_tasks()

    def edit_task(self, event=None):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task, completed = self.tasks[selected_task_index[0]]
            edited_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=task)
            if edited_task is not None:
                confirmed = messagebox.askyesno("Mark as Incomplete", "Mark the task as incomplete?")
                completed = not confirmed
                self.tasks[selected_task_index[0]] = (edited_task, completed)
                self.update_task_list()
                self.save_tasks()

    def mark_as_complete(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task, completed = self.tasks[selected_task_index[0]]
            self.tasks[selected_task_index[0]] = (task, True)
            self.update_task_list()
            self.save_tasks()
            messagebox.showinfo("Completed", f"Task '{task}' marked as complete.")

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task, completed in self.tasks:
            if completed:
                self.task_list.insert(tk.END, f"[Completed] {task}")
                self.task_list.itemconfig(tk.END, {'bg': self.complete_task_color})
            else:
                self.task_list.insert(tk.END, task)
                self.task_list.itemconfig(tk.END, {'bg': self.incomplete_task_color})

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task, completed in self.tasks:
                f.write(f"{task},{completed}\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task, completed = line.strip().split(",")
                    self.tasks.append((task, completed == "True"))
            self.update_task_list()
        except FileNotFoundError:
            pass

    def change_gui_color(self):
        color = colorchooser.askcolor(title="Choose GUI Color")[1]
        if color:
            self.root.config(bg=color)

    def change_button_color(self):
        color = colorchooser.askcolor(title="Choose Button Color")[1]
        if color:
            self.delete_button.config(bg=color)
            self.edit_button.config(bg=color)
            self.complete_button.config(bg=color)
            self.add_button.config(bg=color)

    def change_text_color(self):
        color = colorchooser.askcolor(title="Choose Text Color")[1]
        if color:
            self.task_entry.config(fg=color)
            self.task_list.config(fg=color)

            for i in range(self.task_list.size()):
                self.task_list.itemconfig(i, {'fg': color})

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
