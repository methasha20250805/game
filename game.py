
"""
Game Registration System

Manages Users, Games, and Registrations, all persisted to CSV files.

Files created (in the same folder as this script):
    users.csv          -> user_id, name, email
    games.csv          -> game_id, name, genre
    registrations.csv  -> reg_id, user_id, game_id

"""


import csv
import os
from datetime import datetime

USERS_FILE = "users.csv"
GAMES_FILE = "games.csv"
REGISTRATIONS_FILE = "registrations.csv"


# ---------------------------------------------------------------------------
# Generic CSV helpers
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

USER_HEADERS = ["user_id", "name", "email"]
GAME_HEADERS = ["game_id", "name", "genre"]
REG_HEADERS = ["reg_id", "user_id", "game_id", "timestamp"]

# ---------------------------------------------------------------------------
# User management
# ---------------------------------------------------------------------------

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

def list_users():
    users = read_rows(USERS_FILE)
    if not users:
        print("No users registered yet.\n")
        return
    print("\n--- Users ---")
    for u in users:
        print(f"ID: {u['user_id']} | Name: {u['name']} | Email: {u['email']}")
    print()

# ---------------------------------------------------------------------------
# Game management
# ---------------------------------------------------------------------------

def add_game():
    name = input("Enter game name: ").strip()
    genre = input("Enter game genre: ").strip()

    if not name:
        print("Game name cannot be empty.\n")
        return

    games = read_rows(GAMES_FILE)
    if any(g["name"].lower() == name.lower() for g in games):
        print("A game with this name already exists.\n")
        return

    game_id = next_id(GAMES_FILE, "game_id")
    append_row(GAMES_FILE, {"game_id": game_id, "name": name, "genre": genre}, GAME_HEADERS)
    print(f"Game '{name}' added with ID {game_id}.\n")

def list_games():
    games = read_rows(GAMES_FILE)
    if not games:
        print("No games registered yet.\n")
        return
    print("\n--- Games ---")
    for g in games:
        print(f"ID: {g['game_id']} | Name: {g['name']} | Genre: {g['genre']}")
    print()


# ---------------------------------------------------------------------------
# Registration management (user <-> game)
# ---------------------------------------------------------------------------

def register_user_to_game():
    users = read_rows(USERS_FILE)
    games = read_rows(GAMES_FILE)

    if not users:
        print("No users exist yet. Add a user first.\n")
        return
    if not games:
        print("No games exist yet. Add a game first.\n")
        return

    list_users()
    user_id = input("Enter user ID to register: ").strip()
    if not any(u["user_id"] == user_id for u in users):
        print("Invalid user ID.\n")
        return

    list_games()
    game_id = input("Enter game ID to register for: ").strip()
    if not any(g["game_id"] == game_id for g in games):
        print("Invalid game ID.\n")
        return

    regs = read_rows(REGISTRATIONS_FILE)
    if any(r["user_id"] == user_id and r["game_id"] == game_id for r in regs):
        print("This user is already registered for this game.\n")
        return

    reg_id = next_id(REGISTRATIONS_FILE, "reg_id")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    append_row(
        REGISTRATIONS_FILE,
        {"reg_id": reg_id, "user_id": user_id, "game_id": game_id, "timestamp": timestamp},
        REG_HEADERS,
    )
    print(f"Registration successful (Registration ID {reg_id}).\n")

def list_registrations():
    regs = read_rows(REGISTRATIONS_FILE)
    if not regs:
        print("No registrations yet.\n")
        return

    users = {u["user_id"]: u["name"] for u in read_rows(USERS_FILE)}
    games = {g["game_id"]: g["name"] for g in read_rows(GAMES_FILE)}

    print("\n--- Registrations ---")
    for r in regs:
        uname = users.get(r["user_id"], "Unknown user")
        gname = games.get(r["game_id"], "Unknown game")
        print(f"Reg ID: {r['reg_id']} | User: {uname} | Game: {gname} | When: {r['timestamp']}")
    print()

MENU = """
==== Game Registration System ====
1. Add user
2. List users
3. Add game
4. List games
5. Register a user to a game
6. List registrations
7. Exit
"""

def main():
    init_files()
    while True:
        print(MENU)
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            add_game()
        elif choice == "4":
            list_games()
        elif choice == "5":
            register_user_to_game()
        elif choice == "6":
            list_registrations()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()