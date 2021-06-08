"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by Alejandro Flores Medina

This program implements an awesome version of skeet.

Particle and smoke add it. Original particle and smoke code from Paul Vincent Craven from Arcade https://https://arcade.academy/
"""
from abc import ABC
from abc import abstractmethod

import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15

"""
Particle definitions for explosions 
"""
# How big the particle
PARTICLE_RADIUS = 3

# How many particles per explosion
PARTICLE_COUNT = 20

# Possible particle colors
PARTICLE_COLORS = [arcade.color.ALIZARIN_CRIMSON,
                   arcade.color.COQUELICOT,
                   arcade.color.LAVA,
                   arcade.color.KU_CRIMSON,
                   arcade.color.DARK_TANGERINE]

# How fast the particle moves. Range is from 2.5 <--> 5 with 2.5 and 2.5 set.
PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5

# How fast to fade the particle
PARTICLE_FADE_RATE = 8

# How fast the particle will accelerate down. Make 0 if not desired
PARTICLE_GRAVITY = 0.05

# Chance we'll flip the texture to white and make it 'sparkle'
PARTICLE_SPARKLE_CHANCE = 0.02

"""
Smoke definitions for explosions 
"""
# Rate smoke fades, and rises
SMOKE_FADE_RATE = 7
SMOKE_RISE_RATE = 0.5

# Chance we leave smoke trail
SMOKE_CHANCE = 0.25

# Start scale of smoke, and how fast is scales up
SMOKE_START_SCALE = 0.25
SMOKE_EXPANSION_RATE = 0.03


class Smoke(arcade.SpriteCircle):
    """ This represents a puff of smoke """

    def __init__(self, size):
        super().__init__(size, arcade.color.LIGHT_GRAY, soft=True)
        self.change_y = SMOKE_RISE_RATE
        self.scale = SMOKE_START_SCALE

    def update(self):
        """ Update this particle """
        if self.alpha <= PARTICLE_FADE_RATE:
            # Remove faded out particles
            self.remove_from_sprite_lists()
        else:
            # Update values
            self.alpha -= SMOKE_FADE_RATE
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.scale += SMOKE_EXPANSION_RATE


class Particle(arcade.SpriteCircle):
    """ Explosion particle """

    def __init__(self, my_list):
        # Choose a random color
        color = random.choice(PARTICLE_COLORS)

        # Make the particle
        super().__init__(PARTICLE_RADIUS, color)

        # Track normal particle texture, so we can 'flip' when we sparkle.
        self.normal_texture = self.texture

        # Keep track of the list we are in, so we can add a smoke trail
        self.my_list = my_list

        # Set direction/speed
        speed = random.random() * PARTICLE_SPEED_RANGE + PARTICLE_MIN_SPEED
        direction = random.randrange(360)
        self.change_x = math.sin(math.radians(direction)) * speed
        self.change_y = math.cos(math.radians(direction)) * speed

        # Track original alpha. Used as part of 'sparkle' where we temp set the
        # alpha back to 255
        self.my_alpha = 255

        # What list do we add smoke particles to?
        self.my_list = my_list

    def update(self):
        """ Update the particle """
        if self.my_alpha <= PARTICLE_FADE_RATE:
            # Faded out, remove
            self.remove_from_sprite_lists()
        else:
            # Update
            self.my_alpha -= PARTICLE_FADE_RATE
            self.alpha = self.my_alpha
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.change_y -= PARTICLE_GRAVITY

            # Should we sparkle this?
            if random.random() <= PARTICLE_SPARKLE_CHANCE:
                self.alpha = 255
                self.texture = arcade.make_circle_texture(
                    self.width, arcade.color.WHITE)
            else:
                self.texture = self.normal_texture

            # Leave a smoke particle?
            if random.random() <= SMOKE_CHANCE:
                smoke = Smoke(5)
                smoke.position = self.position
                self.my_list.append(smoke)


class Point(ABC):
    """
    Point class: define a (x, y) point in the screen
    """

    def __init__(self):
        self.x = 0
        self.y = 0   # Default point coordinates(0, 0)


class Velocity(ABC):
    """
    Velocity class: define a dx, dy velocity or change of position in the screen.
    """

    def __init__(self):
        self.dx = 0
        self.dy = 0  # Default Velocity dx, dy (0, 0)


class FlyingObject(ABC):
    """
    FlyingObject class: define a Flying object.
    """

    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    @abstractmethod
    def draw(self):
        pass

    def is_off_screen(self, screen_width, screen_height):
        if ((self.center.x < screen_width) and (self.center.y < screen_height) and
            (self.center.x > 0) and (self.center.y > 0)):
            return False
        else:
            return True


class Bullet(FlyingObject):
    """
    Bullet class: create a bullet.
    """

    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS

    def draw(self):
        arcade.draw_circle_filled(
            self.center.x, self.center.y, self.radius, BULLET_COLOR)

    def fire(self, angle):
        self.center.x = math.cos(math.radians(angle))
        self.center.y = math.sin(math.radians(angle))

        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED


class Target(FlyingObject):
    """
    Target class: create a General target.
    """

    def __init__(self):
        super().__init__()
        self.center.x = random.uniform(0, SCREEN_WIDTH/2)
        self.center.y = random.uniform(SCREEN_HEIGHT/2, SCREEN_HEIGHT)

        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-2, 5)

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def hit(self):
        pass


class standardTarget(Target):
    """
    Standard Target class: create a Standard target.
    """

    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS

    def draw(self):
        arcade.draw_circle_filled(
            self.center.x, self.center.y, self.radius, TARGET_COLOR)

    def hit(self):
        self.alive = False
        return 1


class strongTarget(Target):
    """
    Standard Target class: create a Strong target.
    """

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.radius = TARGET_RADIUS
        self.velocity.dx = random.uniform(1, 3)
        self.velocity.dy = random.uniform(-2, 3)

    def draw(self):

        arcade.draw_circle_outline(
            self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y,
                         TARGET_COLOR, font_size=20)

    def hit(self):
        if self.lives > 1:
            self.lives -= 1
            return 1
        else:
            self.alive = False
            return 5


class safeTarget(Target):
    """
    Standard Target class: create a Safe target.
    """

    def __init__(self):
        super().__init__()
        self.radius = TARGET_SAFE_RADIUS * 2

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, self.radius, self.radius, TARGET_SAFE_COLOR)

    def hit(self):
        self.alive = False
        return -10


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """

    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, 360-self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []

        """
        Add List of Explosions 
        """
        self.explosions_list = []
        self.explosions_list = arcade.SpriteList()

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # TODO: iterate through your targets and draw them...
        for target in self.targets:
            target.draw()

        # Draw explosions
        self.explosions_list.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

        # Update explosions
        self.explosions_list.update()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            target = standardTarget()
        elif randomNumber == 2:
            target = strongTarget()
        else:
            target = safeTarget()
        self.targets.append(target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                            abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

                        # Make an explosion
                        for i in range(PARTICLE_COUNT):
                            particle = Particle(self.explosions_list)
                            particle.center_x = target.center.x
                            particle.center_y = target.center.y
                            self.explosions_list.append(particle)

                            smoke = Smoke(50)
                            smoke.center_x = target.center.x
                            smoke.center_y = target.center.y
                            self.explosions_list.append(smoke)

                            # Hit Sound
                            arcade.sound.play_sound(self.hit_sound)

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        # Gunshot sound
        arcade.sound.play_sound(self.gun_sound)
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.

        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
