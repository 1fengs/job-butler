from pathlib import Path
import csv
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_FILE = BASE_DIR / "applications.csv"


def add_application(company, position, language, photo):

    print(f"Adding application: {company} - {position} - {language} - {'Photo' if photo else 'No Photo'}")
    file_exists = DB_FILE.exists()

    with open(DB_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        if not file_exists:
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