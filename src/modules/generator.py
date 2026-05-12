from pathlib import Path
import shutil
import subprocess

from modules.latex_utils import (
    replace_newcommand,
    switch_language,
    toggle_photo,
    replace_fontawesome
)

from modules.application_db import add_application


BASE_DIR = Path(__file__).resolve().parent.parent.parent

CV_TEMPLATE = BASE_DIR / "templates" / "cv"
COVER_TEMPLATE = BASE_DIR / "templates" / "coverletter"
TEMP_DIR = BASE_DIR / "temp"
OUTPUT_DIR = BASE_DIR / "generated"



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
    with_photo
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
    company_folder = OUTPUT_DIR / company.replace(" ", "_")
    company_folder.mkdir(parents=True, exist_ok=True)

    shutil.copy(
        work_cl / "coverletter-latex.pdf",
        company_folder / f"CoverLetter_{company}.pdf"
    )

    shutil.copy(
        work_cv / "CV-ENDE-AllInkl.pdf",
        company_folder / f"CV_{language}.pdf"
    )

    # Update database
    add_application(
        company,
        position,
        language,
        with_photo
    )