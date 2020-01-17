# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        # Make the player able to carry multiple items
        self.items = []

    def __str__(self):
        info =  f'Name: {self.name} || Current {self.current_room}'

        for i in self.items:
            info += f'{i} '
        return info