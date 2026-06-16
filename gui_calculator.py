import tkinter as tk

window = tk.Tk()
window.title("My Calculator")
window.geometry("350x550")
window.config(bg="lightblue")

display = tk.Entry(window, font=("Arial, 20"), width=15, bd=5, justify="right")
display.pack(pady=20)

def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        answer = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, answer)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

frame = tk.Frame(window, bg="lightblue")
frame.pack()

buttons = [("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3), ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3), ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3), ("C", 3, 0), ("0", 3, 1), ("=", 3, 2), ("+", 3, 3)]

for text, row, col in buttons:
    btn = tk.Button(frame, text=text, font=("Arial, 16"), width=5, height=2, bg="white", command=lambda t=text: calculate() if t=="=" else clear() if t=="C" else click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()    