import tkinter as tk
from tkinter import messagebox


# Function to calculate BMI
def calculate_bmi():
    try:
        # Get user input
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Check if height and weight are positive numbers
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Please enter positive values for weight and height.")
            return

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Display result
        bmi_label.config(text=f"Your BMI: {bmi:.2f}")

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        category_label.config(text=f"Category: {category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")


# Setting up the main window
root = tk.Tk()
root.title("BMI Calculator")

# Setting up the labels and entry fields for weight and height
weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(root, text="Enter your height (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Labels to display the BMI result and category
bmi_label = tk.Label(root, text="Your BMI: ")
bmi_label.grid(row=3, column=0, columnspan=2, pady=5)

category_label = tk.Label(root, text="Category: ")
category_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the Tkinter event loop
root.mainloop()
