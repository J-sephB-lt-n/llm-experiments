from src.obj import Item

class Location:
    """A physical location in the story"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.description = None 
        self.item_contents: list[Item] = [] 
        self.adjacent_locations: list[Location] = []
