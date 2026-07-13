import tkinter as tk

# =====================================
# Calculator Functions
# =====================================

expression = ""
result_displayed = False

def button_click(value):
    global expression, result_displayed
    sval = str(value)
    if result_displayed and sval not in "+-*/":
        expression = ""
        result_displayed = False
    expression += sval
    input_text.set(expression)

def clear():
    global expression, result_displayed
    expression = ""
    result_displayed = False
    input_text.set("")

def calculate():
    global expression, result_displayed

    try:
        # prevent evaluating empty expression
        if not expression:
            input_text.set("")
            return

        # try to evaluate; let exceptions be caught
        result = str(eval(expression))
        input_text.set(result)
        expression = result
        result_displayed = True

    except Exception:
        input_text.set("Error")
        expression = ""
        result_displayed = False

# =====================================
# Main Window
# =====================================

root = tk.Tk()
root.title("Python Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#2C3E50")

# =====================================
# Heading
# =====================================

title_label = tk.Label(
    root,
    text="Hassan First Python Project",
    font=("Arial", 18, "bold"),
    bg="#2C3E50",
    fg="white"
)

title_label.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=(10, 5)
)

# =====================================
# Calculator Name
# =====================================

subtitle_label = tk.Label(
    root,
    text="Calculator",
    font=("Arial", 14, "bold"),
    bg="#2C3E50",
    fg="lightblue"
)

subtitle_label.grid(
    row=1,
    column=0,
    columnspan=4,
    pady=(0, 10)
)

# =====================================
# Display Screen
# =====================================

input_text = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=input_text,
    font=("Arial", 24),
    justify="right",
    bd=8
)

display.grid(
    row=2,
    column=0,
    columnspan=4,
    ipadx=8,
    ipady=20,
    padx=10,
    pady=10,
    sticky="nsew"
)

# =====================================
# Buttons
# =====================================

button_font = ("Arial", 18)

# Row 3
tk.Button(root, text="7", font=button_font,
          command=lambda: button_click(7)).grid(row=3, column=0, sticky="nsew")

tk.Button(root, text="8", font=button_font,
          command=lambda: button_click(8)).grid(row=3, column=1, sticky="nsew")

tk.Button(root, text="9", font=button_font,
          command=lambda: button_click(9)).grid(row=3, column=2, sticky="nsew")

tk.Button(root, text="/", font=button_font,
          command=lambda: button_click("/")).grid(row=3, column=3, sticky="nsew")

# Row 4
tk.Button(root, text="4", font=button_font,
          command=lambda: button_click(4)).grid(row=4, column=0, sticky="nsew")

tk.Button(root, text="5", font=button_font,
          command=lambda: button_click(5)).grid(row=4, column=1, sticky="nsew")

tk.Button(root, text="6", font=button_font,
          command=lambda: button_click(6)).grid(row=4, column=2, sticky="nsew")

tk.Button(root, text="*", font=button_font,
          command=lambda: button_click("*")).grid(row=4, column=3, sticky="nsew")

# Row 5
tk.Button(root, text="1", font=button_font,
          command=lambda: button_click(1)).grid(row=5, column=0, sticky="nsew")

tk.Button(root, text="2", font=button_font,
          command=lambda: button_click(2)).grid(row=5, column=1, sticky="nsew")

tk.Button(root, text="3", font=button_font,
          command=lambda: button_click(3)).grid(row=5, column=2, sticky="nsew")

tk.Button(root, text="-", font=button_font,
          command=lambda: button_click("-")).grid(row=5, column=3, sticky="nsew")

# Row 6
tk.Button(root, text="0", font=button_font,
          command=lambda: button_click(0)).grid(row=6, column=0, sticky="nsew")

tk.Button(root, text=".", font=button_font,
          command=lambda: button_click(".")).grid(row=6, column=1, sticky="nsew")

tk.Button(root, text="C", font=button_font,
          command=clear).grid(row=6, column=2, sticky="nsew")

tk.Button(root, text="+", font=button_font,
          command=lambda: button_click("+")).grid(row=6, column=3, sticky="nsew")

# Equals Button
tk.Button(
    root,
    text="=",
    font=("Arial", 20, "bold"),
    command=calculate
).grid(
    row=7,
    column=0,
    columnspan=4,
    sticky="nsew"
)

# =====================================
# Grid Configuration
# =====================================

for row in range(3, 8):
    root.grid_rowconfigure(row, weight=1)

for col in range(4):
    root.grid_columnconfigure(col, weight=1)

# =====================================
# Run Application
# =====================================

root.mainloop()