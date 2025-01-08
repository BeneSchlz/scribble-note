import customtkinter as ctk

__version__ = "1.0"

def on_closing():
    app.iconify()

def delete_line(event):
    """Delete the entire line where the cursor is located."""
    widget = event.widget
    widget.delete("insert linestart", "insert lineend")
    return "break"

def delete_word(event):
    """Delete the word to the left of the cursor."""
    widget = event.widget
    widget.delete("insert -1c wordstart", "insert")
    return "break"

def delete_title_line(event):
    """Delete the entire text in the title field."""
    title_field.delete(0, "end") 
    return "break"

def delete_title_word(event):
    """Delete the word to the left of the cursor in the title field."""
    cursor_pos = title_field.index("insert")  
    text = title_field.get()  

    if cursor_pos == 0:
        return "break" 

    new_cursor_pos = cursor_pos
    while new_cursor_pos > 0 and text[new_cursor_pos - 1].isspace() is False:
        new_cursor_pos -= 1

    title_field.delete(new_cursor_pos, cursor_pos)
    return "break"


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

    app.destroy()

def cancel_workflow():
    app.destroy()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Scribble")
    app.geometry("700x400")

    app.protocol("WM_DELETE_WINDOW", on_closing)

    title_field = ctk.CTkEntry(app, placeholder_text="Enter your title here", width=650)
    title_field.pack(padx=10, pady=5)

    text_field = ctk.CTkTextbox(app, wrap="word", width=650, height=275)
    text_field.pack(padx=10, pady=10)

    save_button = ctk.CTkButton(
        app,
        text="Save",
        command=save_to_file,
        width=50,
    )
    save_button.place(x=600, y=350)

    cancel_button = ctk.CTkButton(
        app,
        text="Cancel",
        command=cancel_workflow,
        width=50,
    )
    cancel_button.place(x=535, y=350)

    text_field.bind("<Command-BackSpace>", delete_line)
    text_field.bind("<Option-BackSpace>", delete_word)

    title_field.bind("<Command-BackSpace>", delete_title_line)
    title_field.bind("<Option-BackSpace>", delete_title_word)

    app.mainloop()