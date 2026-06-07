import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        self.expression = ""

        self.entry = tk.Entry(
            root,
            font=("Arial", 24),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.entry.pack(fill=tk.BOTH, ipadx=8, ipady=25, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', '%'],
            ['1', '2', '3', '-', '^'],
            ['0', '.', '=', '+', '\\']
        ]

        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both")

        for row in buttons:
            row_frame = tk.Frame(frame)
            row_frame.pack(expand=True, fill="both")

            for button in row:
                btn = tk.Button(
                    row_frame,
                    text=button,
                    font=("Arial", 20),
                    command=lambda b=button: self.click(b)
                )
                btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def click(self, value):
        if value == "C":
            self.expression = ""
            self.update_entry()

        elif value == "=":
            try:
                expression = self.expression.replace("^", "**").replace("\\", "/")
                result = eval(expression)
                self.expression = str(result)
                self.update_entry()
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.update_entry()

        else:
            self.expression += value
            self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
