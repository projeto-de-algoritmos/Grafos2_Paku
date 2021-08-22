from entity import Entity

# Scatter
# Chase
# Frightened
# Eaten

class Ghost(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.mode = "chase"
        self.home = [0, 0]
        self.target = None
        
    def draw(self):
        ...

# O Vermelho
# O target é a posição do Player
class Blinky(Ghost):
    def __init__(self) -> None:
        super().__init__()