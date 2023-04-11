class Boundary:

    def __str__(self) -> str:
        center = str(self.center)
        radius = str(self.radius)
        txt = '>>>'
        txt += ' '
        txt += f'{self.type} boundary'
        txt += ' '
        txt += f'[center: {center}]'
        txt += ' '
        txt += f' [radius: {radius}]'
        return txt

    def __eq__(self, other) -> bool:
        result = False
        if self.__str__() == other.__str__():
            result = True
        return result