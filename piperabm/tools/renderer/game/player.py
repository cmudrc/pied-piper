try: from .foot import Foot
except: from foot import Foot


class Player:

    def __init__(self, index: int):
        self.index = index
        self.feet = {
            'left': Foot(player=self, side='left'),
            'right': Foot(player=self, side='right')
        }
    
    def is_alive(self):
        result = False
        if self.feet['left'].active is True or \
        self.feet['right'].active is True:
            result = True
        return result
    
    def filter_active_feet(self):
        result = []
        foot_left = self.feet['left']
        if foot_left.active is True:
            result.append(foot_left)
        foot_right = self.feet['right']
        if foot_right.active is True:
            result.append(foot_right)
        return result

    def __str__(self):
        txt = 'player ' + str(self.index ) + ': '
        txt += '('
        txt += 'left: ' + str(self.feet['left'].__str__()) + ' '
        txt += 'right: ' + str(self.feet['right'].__str__())
        txt += ')'
        return txt
    

if __name__ == "__main__":
    p = Player(index=1)
    print(p)