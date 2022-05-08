from typing import Optional

from room import Room, RoomManager


class OutputManager:

    def __init__(self, room_manager: RoomManager) -> None:
        self.room_manager: RoomManager = room_manager

    def print_room(self) -> None:
        print(f"You are in {self.room_manager.current_room.description}\n")
        print(f"{self.room_manager.current_room.describe_exits()}\n")

    def print_prompt(self, previous_result: Optional[str]) -> str:
        print("What would you like to do?\n")

        if previous_result:
            print(f"{previous_result}\n")

        return input("> ")
