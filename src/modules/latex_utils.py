from pathlib import Path
import re

def sanitize_text(text: str) -> str:
    if not text:
        return ""

    # Remove emojis / unsupported unicode
    text = text.encode("ascii", "ignore").decode()

    # Escape LaTeX special characters
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text.strip()

def replace_fontawesome(tex_file):
    path = Path(tex_file)
    content = path.read_text()

    updated = re.sub(r"\\usepackage\{fontawesome\}", r"\\usepackage{fontawesome5}", content)

    path.write_text(updated)

def replace_newcommand(tex_file, command_name, new_value):
    path = Path(tex_file)
    content = path.read_text()

    pattern = rf"\\newcommand\{{\\{command_name}\}}\{{.*?\}}"
    replacement = rf"\\newcommand{{\\{command_name}}}{{{new_value}}}"

    updated = re.sub(pattern, replacement, content)

    path.write_text(updated)



def switch_language(tex_file, language="EN"):
    path = Path(tex_file)
    content = path.read_text()

    if language == "EN":
        content = re.sub(r"\\input\{DE\.tex\}", r"\\input{EN.tex}", content)
    else:
        content = re.sub(r"\\input\{EN\.tex\}", r"\\input{DE.tex}", content)

    path.write_text(content)



def toggle_photo(tex_file, language="EN", with_photo=True):
    # path = Path(tex_file)
    # lines = path.read_text().splitlines()

    # updated = []

    # for line in lines:

    #     if "%PHOTO_ON" in line:
    #         if with_photo:
    #             updated.append(line.replace("%", "", 1))
    #         else:
    #             if not line.strip().startswith("%"):
    #                 updated.append("%" + line)
    #             else:
    #                 updated.append(line)

    #     elif "%PHOTO_OFF" in line:
    #         if with_photo:
    #             if not line.strip().startswith("%"):
    #                 updated.append("%" + line)
    #             else:
    #                 updated.append(line)
    #         else:
    #             updated.append(line.replace("%", "", 1))

    #     else:
    #         updated.append(line)

    # path.write_text("\n".join(updated))
    path = Path(tex_file)
    content = path.read_text()
    if with_photo:
        pattern = rf"\\mainbody\{{{language}\}}\{{.*?\}}"
        replacement = rf"\\mainbody{{{language}}}{{WithPhoto}}"
    else:
        pattern = rf"\\mainbody\{{{language}\}}\{{.*?\}}"
        replacement = rf"\\mainbody{{{language}}}{{WithoutPhoto}}"

    updated = re.sub(pattern, replacement, content)

    path.write_text(updated)