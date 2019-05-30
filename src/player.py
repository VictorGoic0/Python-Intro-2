# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def travel(self, direction):
        if (direction == 'n'):
            if (self.current_room.n_to):
                self.current_room = self.current_room.n_to
            else:
                print("There are no more rooms in that directions. Try a different direction.")
        elif (direction == 's'):
            if (self.current_room.s_to):
                self.current_room = self.current_room.s_to
            else:
                print("There are no more rooms in that directions. Try a different direction.")
        elif (direction == 'e'):
            if (self.current_room.e_to):
                self.current_room = self.current_room.e_to
            else:
                print("There are no more rooms in that directions. Try a different direction.")
        elif (direction == 'w'):
            if (self.current_room.w_to):
                self.current_room = self.current_room.w_to
            else:
                print("There are no more rooms in that directions. Try a different direction.")
