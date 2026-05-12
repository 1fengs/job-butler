from pathlib import Path
import sys
import os


# ----------------------------
# APP RESOURCES
# ----------------------------

if getattr(sys, "frozen", False):
    APP_DIR = Path(sys._MEIPASS)
else:
    APP_DIR = Path(__file__).resolve().parent.parent.parent


# ----------------------------
# USER DATA
# ----------------------------

USER_DATA_DIR = Path.home() / "Desktop" / "Wichtige" / "JobHunting" / "JobButlerStorage"

GENERATED_DIR = USER_DATA_DIR / "generated"
TEMP_DIR = USER_DATA_DIR / "temp"

DB_FILE = USER_DATA_DIR / "applications.csv"


# ----------------------------
# TEMPLATES
# ----------------------------

CV_TEMPLATE = APP_DIR / "templates" / "cv"
COVER_TEMPLATE = APP_DIR / "templates" / "coverletter"


# ----------------------------
# CREATE DIRECTORIES
# ----------------------------

GENERATED_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)
USER_DATA_DIR.mkdir(parents=True, exist_ok=True)