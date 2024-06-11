import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        
        # Lista de tarefas
        self.tasks = []
        
        # Elementos da interface
        self.task_label = tk.Label(root, text="Digite a tarefa:")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=15)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.remove_button = tk.Button(root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.grid(row=1, column=2, padx=10, pady=10)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve digitar uma tarefa.")
    
    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para remover.")
    
    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        
        # Lista de tarefas
        self.tasks = []
        
        # Elementos da interface
        self.task_label = tk.Label(root, text="Digite a tarefa:")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=15)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.remove_button = tk.Button(root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.grid(row=1, column=2, padx=10, pady=10)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve digitar uma tarefa.")
    
    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para remover.")
    
    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
