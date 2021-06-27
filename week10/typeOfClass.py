from abc import ABC

class FlyingObject(ABC):
    def __init__(self):
        super().__init__()
    

class Asteroid(FlyingObject):
    def __init__(self):
        super().__init__()

class SmallAsteroid(Asteroid):
    def __init__(self):
        super().__init__()

class MediumAsteroid(Asteroid):
    def __init__(self):
        super().__init__()

class LargeAsteroid(Asteroid):
    def __init__(self):
        super().__init__()



smallRock = SmallAsteroid()
mediumRock = MediumAsteroid()
bigRock = LargeAsteroid()

test = type(smallRock)

print("Type of small Rock: {}" .format(test))