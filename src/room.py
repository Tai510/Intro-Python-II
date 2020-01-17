# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # Make rooms able to hold multiple items
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        info = f"Room: {self.name} || Description: {self.description}\n"

        for i in self.items:
            info += f"Available Items: {i}. {i.description}"
        return info
            