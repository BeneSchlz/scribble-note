import customtkinter as ctk
import os
import sys

LOCK_FILE = "/tmp/scribble_app.lock"

def check_single_instance():
    if os.path.exists(LOCK_FILE):
        print("App is already running.")
        sys.exit()  
    with open(LOCK_FILE, "w") as f:
        f.write(str(os.getpid()))

def clean_up():
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)

def on_closing():
    app.iconify()  

def minimize_with_command_w(event=None):
    app.iconify()  

def delete_line(event):
    widget = event.widget
    widget.delete("insert linestart", "insert lineend")
    return "break"

def delete_word(event):
    widget = event.widget
    widget.delete("insert -1c wordstart", "insert")
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

    app.iconify()  

def cancel_workflow():
    app.iconify()  
if __name__ == "__main__":
    check_single_instance()

    try:
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        app = ctk.CTk()
        app.title("Scribble")
        app.geometry("700x400")

        app.protocol("WM_DELETE_WINDOW", on_closing)

        app.bind("<Command-w>", minimize_with_command_w)

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

        title_field.bind("<Command-BackSpace>", delete_line)
        title_field.bind("<Option-BackSpace>", delete_word)

        app.mainloop() 

    finally:
        clean_up() 