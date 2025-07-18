# --- Game Data Setup ---
# Using a dictionary for rooms makes it easy to look up rooms by name
rooms = {
    "Room A": {
        "name": "Dining Room",
        "description": "You are in a dimly lit dining room. Water drips from the ceiling.",
        "exits": {"west": "Room B", "east": "Room C"},
        "items": ["Torch", "Plate", "Cup"]
    },
    "Room B": {
        "name": "Living Room",
        "description": "You are in a vast living room. A faint light can be seen to the west.",
        "exits": {"east": "Room A", "south": "Room C"},  # Changed exit to match Room A's west
        "items": ["Letter", "Knife", "Statue"]
    },
    "Room C": {
        "name": "Toilet",
        "description": "You are in a small, damp toilet. The air is stale.",
        "exits": {"west": "Room A", "north": "Room B"},  # Changed exit to match Room B's south
        "items": ["Mirror", "ToothBrush", "Pen"]
    }
}

# Player's current location - store the name of the room
current_room_name = "Room A"

# Player's inventory
player_inventory = []

# --- Game Functions ---
def display_room_info(room_name):
    """Displays the current room's name, description, exits, and items."""
    room = rooms[room_name]  # Get the room details from the global 'rooms' dictionary
    print(f"\n--- {room['name']} ---")
    print(room["description"])
    
    # Display exits
    print("Exits:", end=" ")
    if room["exits"]:
        print(", ".join(room["exits"].keys()))
    else:
        print("None")
    
    # Display items
    print("Items:", end=" ")
    if room["items"]:
        print(", ".join(room["items"]))
    else:
        print("None")

def move_player(current_room_name, direction):
    """
    Attempts to move the player in the given direction.
    Returns the new room name if successful, otherwise returns the current room name.
    """
    room = rooms[current_room_name]
    if direction in room["exits"]:
        new_room_name = room["exits"][direction]
        print(f"You move {direction}.")
        return new_room_name
    else:
        print("Invalid direction. You cannot go that way.")
        return current_room_name

def take_item(current_room_name, item_name, inventory):
    """
    Attempts to take an item from the current room and add it to inventory.
    Modifies the room's item list and player's inventory directly.
    """
    room_items = rooms[current_room_name]["items"]
    if item_name in room_items:
        room_items.remove(item_name)
        inventory.append(item_name)
        print(f"You picked up the {item_name}.")
    else:
        print(f"There is no {item_name} here.")

def show_inventory(inventory):
    """Displays the player's current inventory."""
    print("\n--- Your Inventory ---")
    if inventory:
        print(", ".join(inventory))
    else:
        print("Your inventory is empty.")

# --- Main Game Loop ---
print("Welcome to the Simple Adventure Game!")
print("Type 'help' for commands, or 'quit' to exit.")

while True:
    display_room_info(current_room_name)
    command_input = input("\nWhat do you want to do? ").lower().strip()
    parts = command_input.split(" ", 1)
    action = parts[0]
    argument = parts[1] if len(parts) > 1 else None

    if action == "quit":
        print("Thanks for playing!")
        break
    elif action == "go":
        if argument:
            current_room_name = move_player(current_room_name, argument)
        else:
            print("Go where? Please specify a direction (e.g., 'go north').")
    elif action == "take":
        if argument:
            take_item(current_room_name, argument.capitalize(), player_inventory)
        else:
            print("Take what? Please specify an item (e.g., 'take torch').")
    elif action == "inventory":
        show_inventory(player_inventory)
    elif action == "look":
        pass  # Already handled by display_room_info at the start of the loop
    elif action == "help":
        print("\nAvailable commands: go <direction>, take <item>, inventory, look, quit")
    else:
        print("I don't understand that command. Type 'help' for a list of commands.")
