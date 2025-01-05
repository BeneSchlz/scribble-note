import tkinter as tk

def save_to_file():
    title = title_field.get()
    text = text_field.get("1.0", "end-1c")
    filename = f"/Users/benedictschulz/vault_obsidian/{title}.md"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"# {title}\n\n")
            file.write(text)
        print(f"Note saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("scribble")
    root.geometry("500x200")

    button = tk.Button(
        root,
        text = "Save",
        command=save_to_file
    )
    button.pack()


    title_field = tk.Entry(root, width=50)
    title_field.pack(padx=10, pady=5)   

    text_field = tk.Text(root, wrap="word", width=50, height=10)
    text_field.pack(padx=10, pady=10)

    root.mainloop()