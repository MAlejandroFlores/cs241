"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by Alejandro Flores Medina
This program implements the asteroids game.
"""
import arcade
import random
import math
from abc import ABC
from abc import abstractmethod

from arcade import texture


# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


class Point(ABC):
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def set_center(self, x, y):
        pass

    def get_center():
        pass

class Velocity(ABC):
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0

    def set_velocity(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def get_velocity(self):
        velocity = [self.dx, self.dy]
        return velocity

class FlyingObject(ABC):
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.angle = 0
        self.alive = True
        # self.img = "images/playerShip1_orange.png"
        # self.texture = arcade.load_texture(self.img)
        # self.width = self.texture.width
        # self.height = self.texture.height

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, 255)

    def hit(self):
        self.alive =  False

    def is_off_screen(self, screen_width, screen_height):
        if ((self.center.x < screen_width) and (self.center.y < screen_height) and
            (self.center.x > 0) and (self.center.y > 0)):
            return False
        else:
            return True
    
class Asteroids(FlyingObject):
    def __init__(self):
        super().__init__()

    def hit():
        super().hit()

class SmallAsteroid(Asteroids):
    def __init__(self):
        super().__init__()

    def draw(self):
        pass

    def hit():
        super().hit()

class MediumAsteroid(Asteroids):
    def __init__(self):
        super().__init__()

    def draw(self):
        super().draw()
        pass

    def hit(self):
        super().hit()

class LargeAsteroid(Asteroids):
    def __init__(self):
        super().__init__()
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.angle = random.randint(1, 50)
        self.img = "images/meteorGrey_big1.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.radius = BIG_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
        
        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed

    def draw(self):
        super().draw()

        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, 255)

    def hit(self):
        super().hit()

class SpaceShip(FlyingObject):
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH/2
        self.center.y = SCREEN_HEIGHT/2
        self.radius = SHIP_RADIUS
        self.img = "images/playerShip1_orange.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
     
    
    def draw(self):
        super().draw()
        pass

    def hit(self):
        super().hit()


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.asteroids = []
        self.bullets = []

        self.score = 0

        
        for index in range(INITIAL_ROCK_COUNT):
            asteroid = LargeAsteroid()
            self.asteroids.append(asteroid)

        self.spaceship = SpaceShip()


    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        self.spaceship.draw()

        # TODO: draw each object
        for bullet in self.bullets:
            bullet.draw()

        for asteroid in self.asteroids:
            asteroid.draw()

        self.spaceship.draw()
        

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        for bullet in self.bullets:
            bullet.advance()

        for asteroid in self.asteroids:
            asteroid.advance()

        self.spaceship.advance()

        # TODO: Check for collisions

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()