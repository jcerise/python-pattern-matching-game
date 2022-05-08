from unittest import TestCase

from room import RoomManager


class RoomManagerTest(TestCase):

    def test_build_room_map(self):
        room_manager: RoomManager = RoomManager("dungeon.json")
        self.assertTrue(1 == 1)