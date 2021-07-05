"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by Alejandro Flores Medina
This program implements the asteroids game.
"""
from os import remove
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
    '''Point class: Defines a point wioth corrdinates x,y'''
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def set_center(self, x, y):
        '''Setter x,y'''
        pass

    def get_center():
        '''Getter x,y'''
        pass


class Velocity(ABC):
    '''Velocity class:'''
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0

    def set_velocity(self, dx, dy):
        '''Setter: Set velocity dx, dy'''
        self.dx = dx
        self.dy = dy

    def get_velocity(self):
        '''Getter: Get velocity dx, dy'''
        velocity = [self.dx, self.dy]
        return velocity


class FlyingObject(ABC):
    '''Flying Object class: Parent abstract class '''
    def __init__(self):
        '''Constructor method: Define all initial object variables'''
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.angle = 0
        self.speed = 0
        self.alive = True
        # self.img = "images/playerShip1_orange.png"
        # self.texture = arcade.load_texture(self.img)
        # self.width = self.texture.width
        # self.height = self.texture.height

    def advance(self):
        '''Advance method:, move x and y to the current position'''
        if self.center.x < 0: # If the flying Object cross the left side of the screen
            self.center.x += SCREEN_WIDTH # Move the Flying object all the screen to the right
        elif self.center.x > SCREEN_WIDTH: # If the flying Object cross the right side of the screen
            self.center.x -= SCREEN_WIDTH # Move the Flying object all the screen to the left
        else:
            self.center.x += self.velocity.dx # If the object is not on any edge of the right or left screen keep the same coordinates

        if self.center.y < 0: # If the flying Object cross the bottom side of the screen
            self.center.y += SCREEN_HEIGHT # Move the Flying object all the screen to the top
        elif self.center.y > SCREEN_HEIGHT: # If the flying Object cross the top side of the screen
            self.center.y -= SCREEN_HEIGHT # Move the Flying object all the screen to the bottom
        else:
            self.center.y += self.velocity.dy

        self.center.y += self.velocity.dy

    def draw(self):
        '''Draw method: Draw the object based on the texture image'''
        if self.alive:
            arcade.draw_texture_rectangle(
                self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, 255)

    def hit(self):
        '''If the object get hit, dies'''
        self.alive = False


class Bullet(FlyingObject):
    '''Bullet Object, inherit from Flying Parent Object '''
    def __init__(self, angle, x, y):
        '''Bullet's constructor'''
        super().__init__()
        self.radius = BULLET_RADIUS
        self.speed = BULLET_SPEED
        self.life = BULLET_LIFE
        self.angle = angle + 90
        self.center.x = x
        self.center.y = y
        self.img = "images/laserBlue01.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def fire(self, spaceShipVelDx, spaceShipVelDy):
        '''Fire bullet method'''
        '''Set the bullet initial speed, based on the bullet's angle and speed'''
        self.velocity.dx += math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy += math.sin(math.radians(self.angle)) * self.speed
        '''Add the Spaceship initial speed'''
        self.velocity.dx += spaceShipVelDx
        self.velocity.dy += spaceShipVelDy

    def draw(self):
        '''Draw bullet method'''
        super().draw()

    def advance(self):
        '''Advance bullet method'''
        super().advance()
        # print("Bullet life: {}".format(self.life))
        if self.life > 1: # If the bullet still has life
            self.life -= 1 # Decrease bullet's life by one
        elif self.life == 1: # Bullet's last life
            self.life -= 1
            self.alive = False # Kill the bullet


class Asteroids(FlyingObject):
    '''Asteroids Base Object, inherit from Flying Parent Object '''
    def __init__(self):
        '''Constructor: call Parent's constructor'''
        super().__init__()

    def hit(self):
        '''Hit: call Parent's Hit method'''
        super().hit()


class SmallAsteroid(Asteroids):
    '''Small Asteroid class: Inherit from Asteroid Parent Object '''
    def __init__(self):
        super().__init__()
        self.radius = SMALL_ROCK_RADIUS
        self.img = "images/meteorGrey_small1.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        '''Draw: call Parent's Draw method'''
        super().draw()

    def advance(self):
        super().advance()
        self.angle += SMALL_ROCK_SPIN

    def hit(self, asteroids):
        super().hit()


class MediumAsteroid(Asteroids):
    '''Medium Asteroid class: Inherit from Asteroid Parent Object '''
    def __init__(self):
        super().__init__()
        self.radius = MEDIUM_ROCK_RADIUS
        self.img = "images/meteorGrey_med1.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        super().draw()

    def advance(self):
        super().advance()
        self.angle += MEDIUM_ROCK_SPIN

    def hit(self, asteroids):
        super().hit()
        newSmall1 = SmallAsteroid()
        newSmall2 = SmallAsteroid()

        newSmall1.center.x = self.center.x
        newSmall1.center.y = self.center.y
        newSmall1.velocity.dx = self.velocity.dx + 1.5
        newSmall1.velocity.dy = self.velocity.dy + 1.5

        newSmall2.center.x = self.center.x
        newSmall2.center.y = self.center.y
        newSmall2.velocity.dx = self.velocity.dx - 1.5
        newSmall2.velocity.dy = self.velocity.dy - 1.5

        asteroids.append(newSmall1)
        asteroids.append(newSmall2)


class LargeAsteroid(Asteroids):
    '''Large Asteroid class: Inherit from Asteroid Parent Object '''
    def __init__(self):
        super().__init__()
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.radius = BIG_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
        self.angle = random.randint(1, 50)
        self.img = "images/meteorGrey_big1.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed

    def draw(self):
        super().draw()

    def advance(self):
        super().advance()
        self.angle += BIG_ROCK_SPIN

    def hit(self, asteroids):
        super().hit()
        newMedium1 = MediumAsteroid()
        newMedium2 = MediumAsteroid()
        newSmall = SmallAsteroid()

        newMedium1.center.x = self.center.x
        newMedium1.center.y = self.center.y
        newMedium1.velocity.dx = self.velocity.dx
        newMedium1.velocity.dy = self.velocity.dy + 2

        newMedium2.center.x = self.center.x
        newMedium2.center.y = self.center.y
        newMedium2.velocity.dx = self.velocity.dx
        newMedium2.velocity.dy = self.velocity.dy - 2

        newSmall.center.x = self.center.x
        newSmall.center.y = self.center.y
        newSmall.velocity.dx = self.velocity.dx + 5
        newSmall.velocity.dy = self.velocity.dy
        asteroids.append(newMedium1)
        asteroids.append(newMedium2)
        asteroids.append(newSmall)


class SpaceShip(FlyingObject):
    '''Spaceship Object, inherit from Flying Parent Object '''
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH/2
        self.center.y = SCREEN_HEIGHT/2
        self.angle = 0
        self.radius = SHIP_RADIUS
        self.img = "images/playerShip1_orange.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        super().draw()

    def hit(self):
        super().hit()

    def advance(self):
        super().advance()
        # print("Spaceship center X: {}" .format(self.center.x))
        # self.velocity.dx = math.cos(math.radians(self.angle + 90)) * self.speed
        # self.velocity.dy = math.sin(math.radians(self.angle + 90)) * self.speed

    def turnRight(self):
        self.angle -= SHIP_TURN_AMOUNT

    def turnLeft(self):
        self.angle += SHIP_TURN_AMOUNT

    def speedUp(self):
        # self.speed += SHIP_THRUST_AMOUNT
        self.velocity.dx -= math.sin(math.radians(self.angle)
                                     ) * SHIP_THRUST_AMOUNT
        self.velocity.dy += math.cos(math.radians(self.angle)
                                     ) * SHIP_THRUST_AMOUNT

    def speedDown(self):
        # self.speed -= SHIP_THRUST_AMOUNT
        self.velocity.dx += math.sin(math.radians(self.angle)
                                     ) * SHIP_THRUST_AMOUNT
        self.velocity.dy -= math.cos(math.radians(self.angle)
                                     ) * SHIP_THRUST_AMOUNT


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
            if bullet.alive:
                bullet.draw()
            else:
                self.bullets.pop()

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
        self.killZombies()
        self.check_collisions()

    def check_collisions(self):
        '''Check Asteriod hit by bullet'''
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius
                    if ((abs(bullet.center.x - asteroid.center.x) < too_close) and
                            (abs(bullet.center.y - asteroid.center.y) < too_close)):
                        '''It is a Hit!'''
                        print("IT IS A COLLISION!!")
                        print("Asteroid x: {}".format(asteroid.center.x))
                        print("Asteroid y: {}".format(asteroid.center.y))
                        print("Bullet x: {}".format(bullet.center.x))
                        print("Bullet y: {}".format(bullet.center.y))
                        asteroid.hit(self.asteroids)
                        bullet.hit()

        '''Check Ship hit by asteroid'''
        for asteroid in self.asteroids:
            if (self.spaceship.alive and asteroid.alive):
                too_close = self.spaceship.radius + asteroid.radius
                if ((abs(self.spaceship.center.x - asteroid.center.x) < too_close) and
                        (abs(self.spaceship.center.y - asteroid.center.y) < too_close)):
                    '''It is a Hit!'''
                    print("IT IS A SPACESHIP  COLLISION!!")
                    self.spaceship.hit()
                    asteroid.hit(self.asteroids)

    def killZombies(self):
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

        if not self.spaceship.alive:
            pass

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.spaceship.turnLeft()

        if arcade.key.RIGHT in self.held_keys:
            self.spaceship.turnRight()
        if arcade.key.UP in self.held_keys:
            self.spaceship.speedUp()
        if arcade.key.DOWN in self.held_keys:
            self.spaceship.speedDown()

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.spaceship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                newBullet = Bullet(
                    self.spaceship.angle, self.spaceship.center.x, self.spaceship.center.y)
                newBullet.fire(self.spaceship.velocity.dx,
                               self.spaceship.velocity.dy)
                self.bullets.append(newBullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()