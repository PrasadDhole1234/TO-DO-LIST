import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image, ImageTk


class TodoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("300x400")
        self.root.config(bg="darkseagreen")
        self.tasks = []
        try:
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            pass
        self.counter = len(self.tasks) + 1
        self.entry_task = tk.Entry(root, width=30)
        self.entry_task.grid(row=0, column=0, padx=10, pady=10)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="wheat")
        self.add_button.grid(row=0, column=1, padx=5, pady=10)
        self.task_frame = tk.Frame(root, bg="darkseagreen")
        self.task_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.load_tasks()

    def add_task(self):
        task = self.entry_task.get()
        if task.strip() != "":
            self.tasks.append({"id": self.counter, "task": task, "completed": False})
            self.counter += 1
            self.update_task_list()
            self.entry_task.delete(0, tk.END)
            self.save_tasks()

    def update_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        for index, task in enumerate(self.tasks, start=1):
            img_path = "2.jpg" if task["completed"] else "1.png"
            img = Image.open(img_path)
            img = img.resize((20, 20))
            img = ImageTk.PhotoImage(img)
            task_button = tk.Button(self.task_frame, image=img, command=lambda t=task: self.toggle_completion(t),
                                    bg="wheat")
            task_button.image = img
            task_button.grid(row=index, column=0, padx=5, pady=5, sticky="w")
            task_label = tk.Label(self.task_frame, text=f"{index}. {task['task']}", font=("Arial", 12),
                                  bg="darkseagreen")
            task_label.grid(row=index, column=1, padx=5, pady=5, sticky="w")
            delete_button = tk.Button(self.task_frame, text="Delete", command=lambda t=task: self.delete_task(t),
                                      bg="wheat", fg="orangered")
            delete_button.grid(row=index, column=2, padx=5, pady=5, sticky="w")

    def toggle_completion(self, task):
        task["completed"] = not task["completed"]
        self.update_task_list()
        self.save_tasks()

    def delete_task(self, task):
        self.tasks.remove(task)
        self.update_task_list()
        self.save_tasks()

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        self.update_task_list()


root = tk.Tk()
app = TodoApp(root)
root.mainloop()
