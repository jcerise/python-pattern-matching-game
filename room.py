import json
import os
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any


class CardinalDirection(Enum):
    NORTH = "North"
    NORTHEAST = "North East"
    EAST = "East"
    SOUTHEAST = "South East"
    SOUTH = "South"
    SOUTHWEST = "South West"
    WEST = "West"
    NORTHWEST = "North West"


@dataclass(frozen=True)
class RoomExit:
    description: str
    direction: CardinalDirection
    room_id: int


class Room:
    def __init__(self, room_id: int, description: str, exits: Dict[CardinalDirection, RoomExit]) -> None:
        self.room_id: int = room_id
        self.description: str = description
        self.exits: Dict[CardinalDirection, RoomExit] = exits

    def describe(self) -> str:
        return f"{self.description}."

    def describe_exits(self) -> str:
        exits: str = ""
        direction: CardinalDirection
        obvious_exit: RoomExit
        for direction, obvious_exit in self.exits.items():
            exits += f"to the {direction.value.capitalize()}, there is {obvious_exit.description}, "

        # Return a cleaned up version of the string (capitalize, and remove any trailing commas)
        return exits.capitalize()[:-2]


class RoomManager:
    def __init__(self, map_definition: str) -> None:
        self.room_map: Dict[int, Room] = {}
        self.build_room_map(map_definition)

        self.current_room: Room = self.room_map[1]

    def build_room_map(self, map_definition: str) -> None:
        with open(map_definition, "r") as json_file:
            map_data: Dict[str, Dict[str, str]] = json.load(json_file)

        room_id: int
        room_definition: Dict[str, Any]
        for room_id, room_definition in map_data.items():
            try:
                room_id = int(room_id)
                exits_data: List[Dict[str, str]] = room_definition['exits']
            except (ValueError, KeyError):
                # TODO: Handle this
                continue

            exits: Dict[CardinalDirection, RoomExit] = {}
            room_exit: Dict[str, str]
            for room_exit in exits_data:
                try:
                    direction: CardinalDirection = CardinalDirection(room_exit['direction'])
                    constructed_exit: RoomExit = RoomExit(room_exit['description'], direction, int(room_exit["room_id"]))
                    exits[direction] = constructed_exit
                except (ValueError, KeyError):
                    # TODO: Handle this
                    continue

            room: Room = Room(room_id, room_definition["description"], exits)
            self.room_map[room_id] = room

    def exit_current_room(self, direction: CardinalDirection) -> None:
        """
        Transition the room from the current room, to the room in the direction specified by the user, if that direction
        has a valid exit from the current room.

        In addition to updating the current and previous rooms, call any exit hooks for the current room, and andy
        enter hooks for the room being entered.
        """
        if direction in self.current_room.exits.keys():
            room_exit: RoomExit = self.current_room.exits[direction]
            print(f"You move through the {room_exit.description}\n")

            try:
                new_room: Room = self.room_map[room_exit.room_id]
            except IndexError:
                print("""The fabric of reality seems to tear, the room distorts. Despite walking through a door, 
                         you remain where you started.\n""")
                return

            self.current_room = new_room
            print(f"{new_room.describe}")
            return
        else:
            print("You cannot go that way.")
            return

    def print_current_room(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{self.current_room.describe()}\n")

