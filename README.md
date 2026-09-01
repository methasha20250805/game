# Game Registration System

A simple command-line Python program to manage users, games, and user-to-game registrations, with all data persisted in CSV files.

## Features

- Add and list users
- Add and list games
- Register users to games
- List all registrations (with user/game names, not just IDs)
- Prevents duplicate users (by email), duplicate games (by name), and duplicate registrations
- No external dependencies — uses only Python's standard library

## Requirements

- Python 3.6+

## Files

| File | Description |
|---|---|
| `game_registration.py` | The main program |
| `users.csv` | Stores registered users (auto-created) |
| `games.csv` | Stores registered games (auto-created) |
| `registrations.csv` | Stores user-to-game registrations (auto-created) |

These CSV files are created automatically the first time you run the program, in the same folder as the script.

## Usage

Run the program from a terminal:

```bash
python game_registration.py
```

You'll see a menu:

```
==== Game Registration System ====
1. Add user
2. List users
3. Add game
4. List games
5. Register a user to a game
6. List registrations
7. Exit
```

Enter the number of the option you want and follow the prompts.

### Typical workflow

1. **Add a user** (option 1) — enter a name and email.
2. **Add a game** (option 3) — enter a game name and genre.
3. **Register a user to a game** (option 5) — pick a user ID and a game ID from the lists shown.
4. **List registrations** (option 6) — see who's registered for what, and when.

## Data format

**users.csv**
```
user_id,name,email
1,Jane Doe,jane@example.com
```

**games.csv**
```
game_id,name,genre
1,Chess Arena,Strategy
```

**registrations.csv**
```
reg_id,user_id,game_id,timestamp
1,1,1,2026-09-01 12:34:56
```

## Notes

- IDs auto-increment based on existing entries in each CSV file.
- Emails must be unique per user; game names must be unique per game.
- A user cannot register for the same game twice.
- You can open the CSV files directly in Excel, Google Sheets, or any text editor to inspect or back up data.

## Possible extensions

- Delete or edit existing users, games, or registrations
- Email format validation
- Export registration reports
- Simple GUI (e.g. with Tkinter) instead of the CLI menu
