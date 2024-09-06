import tkinter as tk
from tkinter import ttk

def handle_button_click(clicked_button_text):
    current_text = result_var.get()

    #handle if the button is equal
    if clicked_button_text == "=":
        try:
            # replacing calculator representation with python operators
            expression = current_text.replace("÷", "/").replace("x","*")
    
            result = float(eval(expression))
            if result.is_integer():
                result = int(result)
                
            result_var.set(result)

        except Exception as e:
            result_var.set("ERROR")

    #handle if the button is clear
    elif clicked_button_text =="C":
        result_var.set("")
    
    #convert for decimal
    elif clicked_button_text =="%":
        try:
            current_number = float(current_text)
            result_var.set(current_number/100)
        except ValueError:
            result_var.set("ERROR")

    elif clicked_button_text == "±":
        try:
            current_number = float(current_text)
            if current_number.is_integer():
                current_number = int(current_number)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("ERROR")
    else:
        result_var.set(current_text + clicked_button_text)
    

root = tk.Tk()
root.title("Diana's Calculator")

#entry widget to display results
result_var = tk.StringVar()
result_entry = ttk.Entry(root, textvariable = result_var, 
font=("Helvetica", 24), justify = "right")
result_entry.grid(row = 0, column = 0 , columnspan = 4, sticky = "nsew")
buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("x", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2)
]

style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font = ("Helvetica", 16), width = 10, height = 4)
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info)>3 else 1
    button=ttk.Button(root, text = button_text, 
                      command = lambda text=button_text: handle_button_click(text),
                      style ="TButton")
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

width = 500
height = 700
root.geometry(f"{width}x{height}")

root.resizable(False, False)

#keyboard binding
root.bind("<Return>", lambda event: handle_button_click("="))
root.bind("<BackSpace>", lambda event: handle_button_click("C"))
root.bind("<+>", lambda event: handle_button_click("+"))
root.bind("-", lambda event: handle_button_click("-"))
root.bind("<x>", lambda event: handle_button_click("x"))
root.bind("</>", lambda event: handle_button_click("÷"))
root.bind("1", lambda event: handle_button_click("1"))
root.bind("2", lambda event: handle_button_click("2"))
root.bind("3", lambda event: handle_button_click("3"))
root.bind("4", lambda event: handle_button_click("4"))
root.bind("5", lambda event: handle_button_click("5"))
root.bind("6", lambda event: handle_button_click("6"))
root.bind("7", lambda event: handle_button_click("7"))
root.bind("8", lambda event: handle_button_click("8"))
root.bind("9", lambda event: handle_button_click("9"))
root.bind("0", lambda event: handle_button_click("0"))


root.mainloop()