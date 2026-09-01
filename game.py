import csv
import os
from datetime import datetime

USERS_FILE = "users.csv"
GAMES_FILE = "games.csv"
REGISTRATIONS_FILE = "registrations.csv"

def ensure_file(filename, headers):
    """Create the CSV file with headers if it doesn't already exist."""
    if not os.path.exists(filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)

def read_rows(filename):
    with open(filename, "r", newline="", encoding="utf-8") as f:
         return list(csv.DictReader(f))
