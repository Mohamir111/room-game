# 🧭 Text Adventure Game (Python)

A simple terminal-based adventure game built in Python. You can explore different rooms, collect items, and move between locations using simple commands. Great for beginners learning functions, loops, dictionaries, and game logic.

---

## 🎮 Game Overview

You begin in **Room A** (the Dining Room) and can explore other rooms by moving `north`, `south`, `east`, or `west`. Each room has its own description, list of items, and exits.

### 🔑 Features

- Explore connected rooms
- Collect items into your inventory
- Check your current inventory
- Simple command system: `go`, `take`, `inventory`, `look`, `quit`

---

## 🏗️ Game Structure

### Rooms
Defined using a Python dictionary:

```python
rooms = {
    "Room A": {
        "name": "Dining Room",
        "description": "...",
        "exits": {"west": "Room B", "east": "Room C"},
        "items": ["Torch", "Plate", "Cup"]
    },
    ...
}
**Commands**
Command	Description
go east	Move to another room if exit exists
take torch	Pick up an item from the room
inventory	View all items you've picked up
look	Re-display the current room info
quit	Exit the game

▶️ How to Run
Make sure you have Python installed (3.6+ recommended).

Clone the repository:


git clone https://github.com/YOUR_USERNAME/room-game.git
cd room-game
Run the game:

bash
Copy
Edit
python game.py
📚 What You'll Learn
Nested dictionaries

Function definitions and arguments

Loops and conditionals

User input handling

Command-line interaction

💡 Ideas to Improve
Add more rooms and items

Implement locked doors and keys

Add monsters or puzzles

Create a scoring system or win condition

📄 License
This project is open source under the MIT License.

👤 Author
Mohamed Amir Ben Dhief
GitHub: @mohamir111



---



Let me know if you want me to zip it with the game code for upload or help you push it to GitHub.
