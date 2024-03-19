import tkinter as tk

def calculate():
    # Get the input values
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Perform some calculation
    result = num1 + num2

    # Update the output label
    output_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
label1 = tk.Label(root, text="Number 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Number 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Create output label
output_label = tk.Label(root, text="")
output_label.pack()

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Run the application
root.mainloop()