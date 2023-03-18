class Foot:

    def __init__(self, player, side):
        self.player = player
        self.side = side
        self.active = True
    
    def __str__(self):
        return str(self.active)