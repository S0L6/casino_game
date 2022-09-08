# room.py

class Room():

    def __init__(self,room_name):
        # Initilise the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def describe(self):
        # Display a description in the UI. #
        print(f"\nYou are in the {self.name}.") 
        print(self.description)

    def link_rooms(self, room_to_link, direction):
        # links the provided room in the provided direction
        pass

    def move(self, direction):
        # returns the room linked in the given direction
        pass