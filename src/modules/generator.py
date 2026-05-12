from pathlib import Path
import shutil
import subprocess
import os

from modules.latex_utils import (
    replace_newcommand,
    switch_language,
    toggle_photo,
    replace_fontawesome
)

from modules.application_db import add_application


from modules.paths import (
    CV_TEMPLATE,
    COVER_TEMPLATE,
    TEMP_DIR,
    GENERATED_DIR
)



def compile_latex(tex_file, cwd):
    print(f"Compiling {tex_file} in {cwd}...")

    subprocess.run(
        [
            "latexmk",
            "-xelatex",
            tex_file
        ],
        cwd=cwd,
        check=True
    )

    # if result.returncode != 0:
    #     print(result.stdout)
    #     print(result.stderr)
    #     raise Exception("LaTeX compilation failed")
    
    print("Compilation successful")



def generate_application(
    company,
    position,
    language,
    with_photo,
    company_value,
    platform,
    recipient_name,
    job_description,
    misc_notes
):

    work_cv = TEMP_DIR / "cv"
    work_cl = TEMP_DIR / "coverletter"

    if work_cv.exists():
        shutil.rmtree(work_cv)

    if work_cl.exists():
        shutil.rmtree(work_cl)

    shutil.copytree(CV_TEMPLATE, work_cv)
    shutil.copytree(COVER_TEMPLATE, work_cl)

    # Modify cover letter
    cover_file = work_cl / "coverletter-latex.tex"

    replace_newcommand(
        cover_file,
        "CompanyName",
        company
    )

    replace_newcommand(
        cover_file,
        "PositionName",
        position
    )

    replace_newcommand(
        cover_file,
        "CompanyValue",
        company_value
    )

    replace_newcommand(
        cover_file,
        "Platform",
        platform
    )

    replace_newcommand(
        cover_file,
        "RecipientName",
        recipient_name
    )

    # Modify CV
    cv_file = work_cv / "CV-ENDE-AllInkl.tex"
    cv_main_file = work_cv / f"{language}.tex"

    replace_fontawesome(cv_file)
    switch_language(cv_file, language)
    toggle_photo(cv_main_file, language, with_photo)

    # Compile
    compile_latex("coverletter-latex.tex", work_cl)
    compile_latex("CV-ENDE-AllInkl.tex", work_cv)

    # Create output folder
    company_folder = GENERATED_DIR / company.replace(" ", "_")
    company_folder.mkdir(parents=True, exist_ok=True)

    shutil.copy(
        work_cl / "coverletter-latex.pdf",
        company_folder / f"CoverLetter_{company}.pdf"
    )

    shutil.copy(
        work_cv / "CV-ENDE-AllInkl.pdf",
        company_folder / f"CV_{language}.pdf"
    )

    job_description_path = os.path.join(
        company_folder,
        "job_description.txt"
    )

    with open(job_description_path, "w", encoding="utf-8") as f:

        f.write("JOB DESCRIPTION\n")
        f.write("=" * 60)
        f.write("\n\n")

        f.write(job_description)

        f.write("\n\n")
        f.write("=" * 60)
        f.write("\n")
        f.write("MISCELLANEOUS NOTES\n")
        f.write("=" * 60)
        f.write("\n\n")

        for note in misc_notes:
            if note:
                f.write(f"- {note}\n")

    # Update database
    add_application(
        company,
        position,
        language,
        with_photo
    )