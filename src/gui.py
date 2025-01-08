import tkinter as tk

def save_to_file():
    title = title_field.get()
    text = text_field.get("1.0", "end-1c")

    if not title:
        print("Error: Title is empty. Please provide a title.")
        return

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
    root.geometry("700x400")

    button = tk.Button(
        root,
        text = "Save",
        command=save_to_file
    )
    button.place(x=600, y=350)


    title_field = tk.Entry(root, width=500)
    title_field.pack(padx=10, pady=5)   

    text_field = tk.Text(root, wrap="word", width=500, height=10)
    text_field.pack(padx=10, pady=10)

    root.mainloop()