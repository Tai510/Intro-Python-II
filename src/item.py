class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        info = f'{self.name}'
        return info

#  Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser

    def get(self):
        print(f'You picked: {info}')

    def drop(self):
        print(f'You dropped: {info}') 