from tkinter import *

root = Tk()
root.title("Frame Example")
root.config(bg="blue")
left_frame = Frame(root, width=800, height=400, bg="white", relief="solid", bd=2)
left_frame.grid(row=0, column=0, padx=10, pady=5)
left_frame.grid_propagate(False)
root.mainloop()