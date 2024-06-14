import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import os
import json

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x300")
        self.root.configure(background="#f0f0f0")

        self.create_widgets()

        self.data_file = "bmi_data.json"
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as file:
                json.dump([], file)

    def create_widgets(self):
        container = tk.Frame(self.root, bg="#f0f0f0")
        container.place(relx=0.5, rely=0.5, anchor="center")

        title_label = tk.Label(container, text="BMI Calculator", bg="#f0f0f0", font=("Helvetica", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        weight_label = tk.Label(container, text="Weight (kg):", bg="#f0f0f0", font=("Helvetica", 12))
        weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        weight_entry = ttk.Entry(container, font=("Helvetica", 12))
        weight_entry.grid(row=1, column=1, padx=10, pady=5)

        height_label = tk.Label(container, text="Height (m):", bg="#f0f0f0", font=("Helvetica", 12))
        height_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        height_entry = ttk.Entry(container, font=("Helvetica", 12))
        height_entry.grid(row=2, column=1, padx=10, pady=5)

        calculate_button = ttk.Button(container, text="Calculate BMI", command=lambda: self.calculate_bmi(weight_entry, height_entry), style="C.TButton")
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="we")

        self.bmi_label = tk.Label(container, text="", bg="#f0f0f0", font=("Helvetica", 16, "bold"), fg="blue")
        self.bmi_label.grid(row=4, column=0, columnspan=2, pady=5)

        history_button = ttk.Button(container, text="View History", command=self.view_history, style="C.TButton")
        history_button.grid(row=5, column=0, columnspan=2, pady=5, padx=10, sticky="we")

    def calculate_bmi(self, weight_entry, height_entry):
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            bmi = weight / (height ** 2)
            category = self.categorize_bmi(bmi)
            self.bmi_label.config(text=f"BMI: {bmi:.2f} ({category})", fg=self.get_category_color(category))
            self.animate_bmi_text(f"BMI: {bmi:.2f} ({category})")
            self.store_bmi_data(weight, height, bmi, category)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

    def categorize_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def get_category_color(self, category):
        if category == "Underweight":
            return "blue"
        elif category == "Normal weight":
            return "green"
        elif category == "Overweight":
            return "orange"
        else:
            return "red"

    def store_bmi_data(self, weight, height, bmi, category):
        with open(self.data_file, 'r') as file:
            data = json.load(file)
        data.append({"weight": weight, "height": height, "bmi": bmi, "category": category})
        with open(self.data_file, 'w') as file:
            json.dump(data, file)

    def view_history(self):
        with open(self.data_file, 'r') as file:
            data = json.load(file)
        if not data:
            messagebox.showinfo("No data", "No historical data available.")
            return
        weights = [entry["weight"] for entry in data]
        heights = [entry["height"] for entry in data]
        bmis = [entry["bmi"] for entry in data]
        categories = [entry["category"] for entry in data]

        plt.figure(figsize=(10, 6))
        plt.plot(range(len(bmis)), bmis, marker='o', linestyle='-', color='b')
        plt.xlabel("Entry Number")
        plt.ylabel("BMI")
        plt.title("BMI History")
        plt.grid(True)
        plt.show()

    def animate_bmi_text(self, text):
        self.bmi_label.config(text="")
        self.animate_text(text, 0)

    def animate_text(self, text, index):
        if index < len(text):
            self.bmi_label.config(text=text[:index+1])
            self.root.after(100, self.animate_text, text, index+1)

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    style.configure("C.TButton", foreground="black", background="#4CAF50", font=("Helvetica", 12, "bold"))
    app = BMICalculator(root)
    root.mainloop()
