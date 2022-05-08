import os
from typing import Optional

from output import OutputManager
from room import RoomManager, CardinalDirection

room_manager: RoomManager = RoomManager("dungeon.json")
output_manager: OutputManager = OutputManager(room_manager)

action_result: Optional[str] = None
while True:
    # Clear the console
    os.system('clear')

    # Print the contents of the current room (description and exits)
    output_manager.print_room()
    command: str = output_manager.print_prompt(action_result)

    match command.split():
        case ["exit"]:
            print(f"Alright, goodbye!")
            break
        case ["go", direction]:
            try:
                cardinal_direction: CardinalDirection = CardinalDirection(direction.capitalize())
                if cardinal_direction in room_manager.current_room.exits.keys():
                    room_manager.exit_current_room(cardinal_direction)
                    action_result = ""
                else:
                    raise ValueError
            except ValueError:
                action_result = f"{direction} is not a valid way to travel..."
        case [action, obj]:
            action_result = f"Okay, you want to {action} the {obj}."
        case _:
            action_result = f"Sorry, I don't understand..."