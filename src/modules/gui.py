import customtkinter as ctk
from tkinter import messagebox

from modules.generator import generate_application


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



def launch_gui():

    app = ctk.CTk()
    app.geometry("1000x800")
    app.title("Job Butler - Application Package Generator")

    title = ctk.CTkLabel(
        app,
        text="Application Package Generator",
        font=("Arial", 28)
    )

    title.pack(pady=20)

    company_entry = ctk.CTkEntry(
        app,
        width=400,
        placeholder_text="Company Name"
    )

    company_entry.pack(pady=10)

    position_entry = ctk.CTkEntry(
        app,
        width=400,
        placeholder_text="Position Name"
    )

    position_entry.pack(pady=10)

    language_var = ctk.StringVar(value="EN")

    language_label = ctk.CTkLabel(app, text="Language")
    language_label.pack(pady=(20, 5))

    language_menu = ctk.CTkOptionMenu(
        app,
        values=["EN", "DE"],
        variable=language_var
    )

    language_menu.pack(pady=5)

    photo_var = ctk.BooleanVar(value=True)

    photo_checkbox = ctk.CTkCheckBox(
        app,
        text="Include Photo",
        variable=photo_var
    )

    photo_checkbox.pack(pady=20)

    def generate():

        company = company_entry.get()
        position = position_entry.get()

        if not company or not position:
            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )
            return

        try:
            generate_application(
                company=company,
                position=position,
                language=language_var.get(),
                with_photo=photo_var.get()
            )

            messagebox.showinfo(
                "Success",
                f"Application generated for {company}"
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    generate_button = ctk.CTkButton(
        app,
        text="Generate Application",
        command=generate,
        width=300,
        height=50
    )

    generate_button.pack(pady=40)

    app.mainloop()