from pathlib import Path
import csv
from datetime import datetime

from modules.paths import DB_FILE


def add_application(company, position, language, photo):

    existing_rows = []

    if DB_FILE.exists():
        with open(DB_FILE, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            existing_rows = list(reader)

            for row in existing_rows[1:]:
                if (
                    row[0] == company and
                    row[1] == position and
                    row[3] == language
                ):
                    print("Application already exists.")
                    return

    with open(DB_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        if not existing_rows:
            writer.writerow([
                "company",
                "position",
                "date",
                "language",
                "photo"
            ])

        writer.writerow([
            company,
            position,
            datetime.now().strftime("%Y-%m-%d"),
            language,
            "YES" if photo else "NO"
        ])