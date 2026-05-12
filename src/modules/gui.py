import customtkinter as ctk
from tkinter import messagebox
import threading

from modules.generator import generate_application


# ---------------------------------------------------
# APP CONFIG
# ---------------------------------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ---------------------------------------------------
# MAIN GUI
# ---------------------------------------------------

def launch_gui():

    app = ctk.CTk()

    app.title("Job Butler")
    app.geometry("1920x1080")
    app.minsize(900, 620)

    # Colors
    BG_COLOR = "#0f172a"
    CARD_COLOR = "#111827"
    INPUT_COLOR = "#1f2937"
    TEXT_MUTED = "#94a3b8"
    ACCENT = "#3b82f6"

    app.configure(fg_color=BG_COLOR)

    # ---------------------------------------------------
    # LAYOUT
    # ---------------------------------------------------

    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)

    app.grid_rowconfigure(0, weight=1)

    # ---------------------------------------------------
    # LEFT PANEL
    # ---------------------------------------------------

    left_frame = ctk.CTkFrame(
        app,
        fg_color=BG_COLOR,
        corner_radius=0
    )

    left_frame.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=(40, 20),
        pady=40
    )

    # Logo / Header

    logo_label = ctk.CTkLabel(
        left_frame,
        text="JOB BUTLER",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color=ACCENT
    )

    logo_label.pack(anchor="w", pady=(20, 10))

    title_label = ctk.CTkLabel(
        left_frame,
        text="Application\nPackage Generator",
        justify="left",
        font=ctk.CTkFont(size=42, weight="bold")
    )

    title_label.pack(anchor="w")

    subtitle_label = ctk.CTkLabel(
        left_frame,
        text=(
            "Generate modern application packages\n"
            "including CV and cover letter in seconds."
        ),
        justify="left",
        text_color=TEXT_MUTED,
        font=ctk.CTkFont(size=16)
    )

    subtitle_label.pack(anchor="w", pady=(20, 0))

    # ---------------------------------------------------
    # JOB DESCRIPTION PANEL
    # ---------------------------------------------------

    job_box = ctk.CTkFrame(
        left_frame,
        fg_color="#172033",
        corner_radius=20
    )

    job_box.pack(
        fill="both",
        expand=True,
        pady=(40, 0)
    )

    # Title

    job_title = ctk.CTkLabel(
        job_box,
        text="Job Description",
        font=ctk.CTkFont(size=20, weight="bold")
    )

    job_title.pack(anchor="w", padx=25, pady=(25, 10))

    job_subtitle = ctk.CTkLabel(
        job_box,
        text="Paste the full job posting here",
        text_color=TEXT_MUTED,
        font=ctk.CTkFont(size=13)
    )

    job_subtitle.pack(anchor="w", padx=25)

    # ---------------------------------------------------
    # JOB DESCRIPTION TEXTBOX
    # ---------------------------------------------------

    job_description_text = ctk.CTkTextbox(
        job_box,
        height=260,
        corner_radius=14,
        border_width=1,
        border_color="#334155",
        fg_color="#0f172a",
        font=ctk.CTkFont(size=14),
        wrap="word"
    )

    job_description_text.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=(20, 20)
    )

    # ---------------------------------------------------
    # NOTES SECTION
    # ---------------------------------------------------

    notes_label = ctk.CTkLabel(
        job_box,
        text="Miscellaneous Notes",
        font=ctk.CTkFont(size=16, weight="bold")
    )

    notes_label.pack(anchor="w", padx=25, pady=(0, 12))

    # Note 1

    note1_entry = ctk.CTkEntry(
        job_box,
        height=46,
        corner_radius=12,
        border_width=1,
        fg_color=INPUT_COLOR,
        border_color="#334155",
        placeholder_text="Additional note...",
        font=ctk.CTkFont(size=14)
    )

    note1_entry.pack(fill="x", padx=25, pady=(0, 12))

    # Note 2

    note2_entry = ctk.CTkEntry(
        job_box,
        height=46,
        corner_radius=12,
        border_width=1,
        fg_color=INPUT_COLOR,
        border_color="#334155",
        placeholder_text="Additional note...",
        font=ctk.CTkFont(size=14)
    )

    note2_entry.pack(fill="x", padx=25, pady=(0, 25))

    # ---------------------------------------------------
    # RIGHT PANEL
    # ---------------------------------------------------

    right_frame = ctk.CTkFrame(
        app,
        fg_color=CARD_COLOR,
        corner_radius=28,
        border_width=1,
        border_color="#1e293b"
    )

    right_frame.grid(
        row=0,
        column=1,
        sticky="nsew",
        padx=(20, 40),
        pady=40
    )

    right_frame.grid_columnconfigure(0, weight=1)

    # Form title

    form_title = ctk.CTkLabel(
        right_frame,
        text="Create New Application",
        font=ctk.CTkFont(size=28, weight="bold")
    )

    form_title.pack(anchor="w", padx=40, pady=(40, 8))

    form_subtitle = ctk.CTkLabel(
        right_frame,
        text="Fill in the details below",
        text_color=TEXT_MUTED,
        font=ctk.CTkFont(size=14)
    )

    form_subtitle.pack(anchor="w", padx=40, pady=(0, 30))

    # ---------------------------------------------------
    # COMPANY
    # ---------------------------------------------------

    company_label = ctk.CTkLabel(
        right_frame,
        text="Company Name",
        anchor="w",
        font=ctk.CTkFont(size=14, weight="bold")
    )

    company_label.pack(anchor="w", padx=40)

    company_entry = ctk.CTkEntry(
        right_frame,
        height=52,
        corner_radius=14,
        border_width=1,
        fg_color=INPUT_COLOR,
        border_color="#334155",
        placeholder_text="Enter company name",
        font=ctk.CTkFont(size=15)
    )

    company_entry.pack(fill="x", padx=40, pady=(8, 24))

    # ---------------------------------------------------
    # POSITION
    # ---------------------------------------------------

    position_label = ctk.CTkLabel(
        right_frame,
        text="Position",
        anchor="w",
        font=ctk.CTkFont(size=14, weight="bold")
    )

    position_label.pack(anchor="w", padx=40)

    position_entry = ctk.CTkEntry(
        right_frame,
        height=52,
        corner_radius=14,
        border_width=1,
        fg_color=INPUT_COLOR,
        border_color="#334155",
        placeholder_text="Enter position title",
        font=ctk.CTkFont(size=15)
    )

    position_entry.pack(fill="x", padx=40, pady=(8, 24))

    # ---------------------------------------------------
    # COMPANY VALUE
    # ---------------------------------------------------

    company_value_label = ctk.CTkLabel(
        right_frame,
        text="Company Value",
        anchor="w",
        font=ctk.CTkFont(size=14, weight="bold")
    )

    company_value_label.pack(anchor="w", padx=40)

    company_value_entry = ctk.CTkEntry(
        right_frame,
        height=52,
        corner_radius=14,
        border_width=1,
        fg_color=INPUT_COLOR,
        border_color="#334155",
        placeholder_text="Innovation, Sustainability, AI, etc.",
        font=ctk.CTkFont(size=15)
    )

    company_value_entry.pack(fill="x", padx=40, pady=(8, 24))


    # ---------------------------------------------------
    # JOB PLATFORM
    # ---------------------------------------------------

    platform_label = ctk.CTkLabel(
        right_frame,
        text="Job Platform",
        anchor="w",
        font=ctk.CTkFont(size=14, weight="bold")
    )

    platform_label.pack(anchor="w", padx=40)

    platform_entry = ctk.CTkEntry(
        right_frame,
        height=52,
        corner_radius=14,
        border_width=1,
        fg_color=INPUT_COLOR,
        border_color="#334155",
        font=ctk.CTkFont(size=15)
    )

    platform_entry.insert(0, "LinkedIn")

    platform_entry.pack(fill="x", padx=40, pady=(8, 24))


    # ---------------------------------------------------
    # RECIPIENT NAME
    # ---------------------------------------------------

    recipient_label = ctk.CTkLabel(
        right_frame,
        text="Recipient Name",
        anchor="w",
        font=ctk.CTkFont(size=14, weight="bold")
    )

    recipient_label.pack(anchor="w", padx=40)

    recipient_entry = ctk.CTkEntry(
        right_frame,
        height=52,
        corner_radius=14,
        border_width=1,
        fg_color=INPUT_COLOR,
        border_color="#334155",
        font=ctk.CTkFont(size=15)
    )

    recipient_entry.insert(0, "Recruiting Team")

    recipient_entry.pack(fill="x", padx=40, pady=(8, 24))

    # ---------------------------------------------------
    # LANGUAGE
    # ---------------------------------------------------

    language_label = ctk.CTkLabel(
        right_frame,
        text="Language",
        anchor="w",
        font=ctk.CTkFont(size=14, weight="bold")
    )

    language_label.pack(anchor="w", padx=40)

    language_var = ctk.StringVar(value="EN")

    language_selector = ctk.CTkSegmentedButton(
        right_frame,
        values=["EN", "DE"],
        variable=language_var,
        height=42,
        corner_radius=12,
        selected_color=ACCENT,
        selected_hover_color="#2563eb",
        unselected_color="#1e293b",
        unselected_hover_color="#334155",
        font=ctk.CTkFont(size=14, weight="bold")
    )

    language_selector.pack(fill="x", padx=40, pady=(10, 30))

    # ---------------------------------------------------
    # PHOTO CHECKBOX
    # ---------------------------------------------------

    photo_var = ctk.BooleanVar(value=True)

    photo_checkbox = ctk.CTkCheckBox(
        right_frame,
        text="Include Profile Photo",
        variable=photo_var,
        checkbox_width=22,
        checkbox_height=22,
        corner_radius=6,
        border_width=2,
        font=ctk.CTkFont(size=14)
    )

    photo_checkbox.pack(anchor="w", padx=40, pady=(0, 30))

    # ---------------------------------------------------
    # STATUS LABEL
    # ---------------------------------------------------

    status_label = ctk.CTkLabel(
        right_frame,
        text="Ready",
        text_color=TEXT_MUTED,
        font=ctk.CTkFont(size=13)
    )

    status_label.pack(anchor="w", padx=40, pady=(0, 20))

    # ---------------------------------------------------
    # GENERATE FUNCTION
    # ---------------------------------------------------

    def run_generation():

        company = company_entry.get().strip()
        position = position_entry.get().strip()

        if not company or not position:
            messagebox.showerror(
                "Missing Information",
                "Please fill in all fields."
            )
            return

        generate_button.configure(
            state="disabled",
            text="Generating..."
        )

        status_label.configure(
            text="Generating application package..."
        )

        def worker():

            try:
                
                job_description = job_description_text.get("1.0", "end").strip()

                misc_notes = [
                    note1_entry.get().strip(),
                    note2_entry.get().strip()
                ]

                generate_application(
                    company=company,
                    position=position,
                    language=language_var.get(),
                    with_photo=photo_var.get(),
                    company_value=company_value_entry.get().strip(),
                    platform=platform_entry.get().strip(),
                    recipient_name=recipient_entry.get().strip(),
                    job_description=job_description,
                    misc_notes=misc_notes
                )

                app.after(
                    0,
                    lambda: status_label.configure(
                        text=f"Successfully generated application for {company}"
                    )
                )

                app.after(
                    0,
                    lambda: messagebox.showinfo(
                        "Success",
                        f"Application successfully generated for:\n\n{company}"
                    )
                )

            except Exception as e:

                app.after(
                    0,
                    lambda: messagebox.showerror(
                        "Error",
                        str(e)
                    )
                )

                app.after(
                    0,
                    lambda: status_label.configure(
                        text="Generation failed"
                    )
                )

            finally:

                app.after(
                    0,
                    lambda: generate_button.configure(
                        state="normal",
                        text="Generate Application"
                    )
                )

        threading.Thread(
            target=worker,
            daemon=True
        ).start()

    # ---------------------------------------------------
    # GENERATE BUTTON
    # ---------------------------------------------------

    generate_button = ctk.CTkButton(
        right_frame,
        text="Generate Application",
        command=run_generation,
        height=56,
        corner_radius=16,
        fg_color=ACCENT,
        hover_color="#2563eb",
        font=ctk.CTkFont(size=16, weight="bold")
    )

    generate_button.pack(
        fill="x",
        padx=40,
        pady=(10, 40)
    )

    # ---------------------------------------------------
    # START APP
    # ---------------------------------------------------

    app.mainloop()