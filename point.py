

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return '({0}, {1})'.format(self.x, self.y)