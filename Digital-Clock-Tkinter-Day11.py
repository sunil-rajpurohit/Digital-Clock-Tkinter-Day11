import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)


root = tk.Tk()
root.title("12-Hour Digital Clock")
root.geometry("350x120")
root.resizable(False, False)

root.configure(bg="black")
time_label = tk.Label(
    root,
    font=("Digital-7", 36, "bold"), 
    bg="black",
    fg="lime"
)
time_label.pack(expand=True)


update_time()


root.mainloop()
