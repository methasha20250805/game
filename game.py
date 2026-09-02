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


def append_row(filename, row_dict, headers):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow(row_dict)


def next_id(filename, id_field):
    rows = read_rows(filename)
    if not rows:
        return 1
    return max(int(r[id_field]) for r in rows) + 1

USER_HEADERS = ["user_id", "name", "email"]
GAME_HEADERS = ["game_id", "name", "genre"]
REG_HEADERS = ["reg_id", "user_id", "game_id", "timestamp"]

def init_files():
    ensure_file(USERS_FILE, USER_HEADERS)
    ensure_file(GAMES_FILE, GAME_HEADERS)
    ensure_file(REGISTRATIONS_FILE, REG_HEADERS)

def add_user():
    name = input("Enter user name: ").strip()
    email = input("Enter user email: ").strip()

    if not name or not email:
        print("Name and email cannot be empty.\n")
        return

    # Prevent duplicate emails
    users = read_rows(USERS_FILE)
    if any(u["email"].lower() == email.lower() for u in users):
        print("A user with this email already exists.\n")
        return

    user_id = next_id(USERS_FILE, "user_id")
    append_row(USERS_FILE, {"user_id": user_id, "name": name, "email": email}, USER_HEADERS)
    print(f"User '{name}' added with ID {user_id}.\n")