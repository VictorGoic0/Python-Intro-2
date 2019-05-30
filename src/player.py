# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def getCurrentRoom(self):
        print(f'\n***** Current Room: {self.current_room.name} *****\n')
        print(f'\n***** Current Description: {self.current_room.description} *****\n')
    def noRooms(self):
        print("There are no more rooms in that directions. Try a different direction.")
    def travel(self, direction):
        if (direction == 'n'):
            if (self.current_room.n_to):
                self.current_room = self.current_room.n_to
                self.getCurrentRoom()
            else:
                self.noRooms()
        elif (direction == 's'):
            if (self.current_room.s_to):
                self.current_room = self.current_room.s_to
                self.getCurrentRoom()
            else:
                self.noRooms()
        elif (direction == 'e'):
            if (self.current_room.e_to):
                self.current_room = self.current_room.e_to
                self.getCurrentRoom()
            else:
                self.noRooms()
        elif (direction == 'w'):
            if (self.current_room.w_to):
                self.current_room = self.current_room.w_to
                self.getCurrentRoom()
            else:
                self.noRooms()
