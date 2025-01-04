import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("scribble")
    root.geometry("500x200")

    button = tk.Button(
        root,
        text = "Save"
    )
    button.pack()


    title_field = tk.Entry(root, width=50)
    title_field.pack(padx=10, pady=5)   

    text_field = tk.Text(root, wrap="word", width=50, height=10)
    text_field.pack(padx=10, pady=10)

    root.mainloop()