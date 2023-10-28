from typing import List

class Forest:
    def __init__(self) -> None:
        self.trees: List["Tree"] = []

    def plant_tree(self, name: str, color: str, x: int, y: int):
        tree_type = TreeTypeFactory.get_tree_type(name, color)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self): 
        for tree in self.trees:
            tree.draw()

class Tree:
    def __init__(self, x: int, y: int, type: "TreeType") -> None:
        self.x = x
        self.y = y
        self.type = type
    
    def draw(self):
        return self.type.draw(self.x, self.y)
    
class TreeType:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color
        self.image = self.get_image(name, color)

    def get_image(self, name: str, color: str) -> bytes: ...

    def draw(x: int, y: int): ...
        # draw image at coordinates

class TreeTypeFactory:
    tree_types: List[TreeType] = []

    @classmethod
    def get_tree_type(self, name: str, color: str) -> TreeType:
        for tree_type in self.tree_types:
            if tree_type.name == name and tree_type.color == color:
                return tree_type
        tree_type = TreeType(name, color)
        self.tree_types.append(tree_type)