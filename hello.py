import tkinter as tk

def submit_form():
    # This function will be called when the Submit button is clicked
    name = entry_name.get()
    age = entry_age.get()
    print(f"Name: {name}, Age: {age}")

# Create the main window
root = tk.Tk()
root.title("Simple Form")

# Create labels and entry widgets for the form
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0, padx=10, pady=10)

entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=10)

# Create a Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()

