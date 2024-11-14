def main():
    current_room = "entrance"
    inventory = []

    rooms = {
        "entrance": {
            "description": "You are at the entrance of a dark cave.",
            "exits": {"north": "hallway"},
            "item": None
        },
        "hallway": {
            "description": "You are in a long hallway. There is a door to the south.",
            "exits": {"south": "entrance", "north": "treasure_room"},
            "item": "gold coin"
        },
        "treasure_room": {
            "description": "You found the treasure room! It's filled with gold!",
            "exits": {"south": "hallway"},
            "item": None
        }
    }

    while True:
        print("\n" + rooms[current_room]["description"])
        if rooms[current_room]["item"]:
            print(f"You see a {rooms[current_room]['item']} here.")
        
        command = input("What do you want to do? (move [direction], take [item], inventory, exit): ").strip().lower()
        
        if command.startswith("move"):
            direction = command.split(" ")[1]
            if direction in rooms[current_room]["exits"]:
                current_room = rooms[current_room]["exits"][direction]
            else:
                print("You can't go that way.")
        
        elif command.startswith("take"):
            item = command.split(" ")[1]
            if item == rooms[current_room]["item"]:
                inventory.append(item)
                rooms[current_room]["item"] = None
                print(f"You took the {item}.")
            else:
                print("There is no such item here.")
        
        elif command == "inventory":
            print("You have: " + ", ".join(inventory) if inventory else "Your inventory is empty.")
        
        elif command == "exit":
            print("Exiting the game.")
            break
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
