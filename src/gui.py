import customtkinter as ctk

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
    title_field.delete(0, "end")  # Clear all text in the entry field
    return "break"

def delete_title_word(event):
    """Delete the word to the left of the cursor in the title field."""
    cursor_pos = title_field.index("insert")  # Get the current cursor position
    text = title_field.get()  # Get the current text in the entry field

    if cursor_pos == 0:
        return "break"  # If the cursor is at the start, do nothing

    # Find the start of the last word
    new_cursor_pos = cursor_pos
    while new_cursor_pos > 0 and text[new_cursor_pos - 1].isspace() is False:
        new_cursor_pos -= 1

    # Delete from the start of the word to the cursor
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
    # Initialize CustomTkinter
    ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

    app = ctk.CTk()  # Use CTk instead of Tk
    app.title("Scribble")
    app.geometry("700x400")

    # Title Entry Field
    title_field = ctk.CTkEntry(app, placeholder_text="Enter your title here", width=650)
    title_field.pack(padx=10, pady=5)

    # Text Field for Content
    text_field = ctk.CTkTextbox(app, wrap="word", width=650, height=275)
    text_field.pack(padx=10, pady=10)

    # Save Button
    save_button = ctk.CTkButton(
        app,
        text="Save",
        command=save_to_file,
        width=50,
    )
    save_button.place(x=600, y=350)

    # Cancel Button
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