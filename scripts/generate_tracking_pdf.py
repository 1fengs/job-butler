import csv

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

CSV_FILE = "applications.csv"
PDF_FILE = "applications_tracker.pdf"

styles = getSampleStyleSheet()

# -----------------------------
# TABLE CONFIG
# -----------------------------

COL_WIDTHS = [
    180,  # company
    260,  # position
    85,   # date
    65,   # reply
    90,   # 1st
    90    # 2nd
]

ROW_HEIGHT = 32

PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)

LEFT_MARGIN = 50
RIGHT_MARGIN = 50
TOP_MARGIN = 50
BOTTOM_MARGIN = 50

TABLE_WIDTH = sum(COL_WIDTHS)

# center table horizontally
TABLE_X = (PAGE_WIDTH - TABLE_WIDTH) / 2


def load_csv():
    rows = []

    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append([
                Paragraph(
                    f"<font size=9>{row['company']}</font>",
                    styles["BodyText"]
                ),
                Paragraph(
                    f"<font size=9>{row['position']}</font>",
                    styles["BodyText"]
                ),
                row["date"],
                "",
                "",
                ""
            ])

    return rows


csv_rows = load_csv()


def draw_checkboxes(canvas, doc):

    form = canvas.acroForm

    # Calculate table top position
    table_top_y = PAGE_HEIGHT - TOP_MARGIN - 85

    for i in range(len(csv_rows)):

        # row y position
        y = table_top_y - ((i + 1) * ROW_HEIGHT) + 10

        # Reply checkbox
        form.checkbox(
            name=f"reply_{i}",
            x=TABLE_X + sum(COL_WIDTHS[:3]) + 30,
            y=y,
            size=12,
            buttonStyle='check',
            borderWidth=1,
            borderColor=colors.HexColor("#9CA3AF"),
            forceBorder=True
        )

        # First interview
        form.checkbox(
            name=f"first_{i}",
            x=TABLE_X + sum(COL_WIDTHS[:4]) + 40,
            y=y,
            size=12,
            buttonStyle='check',
            borderWidth=1,
            borderColor=colors.HexColor("#9CA3AF"),
            forceBorder=True
        )

        # Second interview
        form.checkbox(
            name=f"second_{i}",
            x=TABLE_X + sum(COL_WIDTHS[:5]) + 40,
            y=y,
            size=12,
            buttonStyle='check',
            borderWidth=1,
            borderColor=colors.HexColor("#9CA3AF"),
            forceBorder=True
        )


doc = SimpleDocTemplate(
    PDF_FILE,
    pagesize=landscape(A4),

    leftMargin=LEFT_MARGIN,
    rightMargin=RIGHT_MARGIN,
    topMargin=TOP_MARGIN,
    bottomMargin=BOTTOM_MARGIN
)

elements = []

title = Paragraph(
    "<font size=20><b>Job Application Tracker</b></font>",
    styles["Title"]
)

elements.append(title)
elements.append(Spacer(1, 20))

data = [[
    "Company",
    "Position",
    "Date",
    "Reply",
    "1st Interview",
    "2nd Interview"
]]

data.extend(csv_rows)

table = Table(
    data,
    colWidths=COL_WIDTHS,
    rowHeights=[ROW_HEIGHT] * (len(data)),
    repeatRows=1,

    # Explicit centering
    hAlign='CENTER'
)

table.setStyle(TableStyle([

    # Header
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F2937")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),

    # Body
    ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F9FAFB")),

    # Soft grid
    ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#D1D5DB")),

    # Padding
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),

    # Alignment
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
]))

elements.append(table)

doc.build(
    elements,
    onFirstPage=draw_checkboxes,
    onLaterPages=draw_checkboxes
)

print(f"Generated: {PDF_FILE}")