asteroids.py                                                                                        000644  000765  000024  00000032223 14066543253 015754  0                                                                                                    ustar 00alejandroflores                 staff                           000000  000000                                                                                                                                                                         """
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
        self.speed = 0
        self.alive = True
        # self.img = "images/playerShip1_orange.png"
        # self.texture = arcade.load_texture(self.img)
        # self.width = self.texture.width
        # self.height = self.texture.height

    def advance(self):

        if self.center.x < 0:
            self.center.x += SCREEN_WIDTH
        elif self.center.x > SCREEN_WIDTH:
            self.center.x -= SCREEN_WIDTH
        else:
            self.center.x += self.velocity.dx

        if self.center.y < 0:
            self.center.y += SCREEN_HEIGHT
        elif self.center.y > SCREEN_HEIGHT:
            self.center.y -= SCREEN_HEIGHT
        else:
            self.center.y += self.velocity.dy

        self.center.y += self.velocity.dy

    def draw(self):
        if self.alive:
            arcade.draw_texture_rectangle(
                self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, 255)

    def hit(self):
        self.alive = False


class Bullet(FlyingObject):
    def __init__(self, angle, x, y):
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
        self.velocity.dx += math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy += math.sin(math.radians(self.angle)) * self.speed
        self.velocity.dx += spaceShipVelDx
        self.velocity.dy += spaceShipVelDy

    def draw(self):
        super().draw()

    def advance(self):
        super().advance()
        # print("Bullet life: {}".format(self.life))
        if self.life > 1:
            self.life -= 1
        elif self.life == 1:
            self.life -= 1
            self.alive = False


class Asteroids(FlyingObject):
    def __init__(self):
        super().__init__()

    def hit(self):
        super().hit()


class SmallAsteroid(Asteroids):
    def __init__(self):
        super().__init__()
        self.radius = SMALL_ROCK_RADIUS
        self.img = "images/meteorGrey_small1.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        super().draw()

    def advance(self):
        super().advance()
        self.angle += SMALL_ROCK_SPIN

    def hit(self, asteroids):
        super().hit()


class MediumAsteroid(Asteroids):
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
                                                                                                                                                                                                                                                                                                                                                                             images/                                                                                             000755  000765  000024  00000000000 14066014314 014637  5                                                                                                    ustar 00alejandroflores                 staff                           000000  000000                                                                                                                                                                         images/.DS_Store                                                                                    000644  000765  000024  00000014004 14066014314 016321  0                                                                                                    ustar 00alejandroflores                 staff                           000000  000000                                                                                                                                                                            Bud1            %                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 @      ?                                        @      ?                                          @      ?                                          @                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   E   %                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       DSDB                             `          ?                                           @      ?                                          @      ?                                          @                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          images/laserBlue01.png                                                                              000644  000765  000024  00000001165 14066014314 017427  0                                                                                                    ustar 00alejandroflores                 staff                           000000  000000                                                                                                                                                                         ?PNG

   IHDR   6   	   yi??   	pHYs  ?  ??+   tIME?#???L   tEXtAuthor ???H   tEXtDescription 	!#   
tEXtCopyright ??:   tEXtCreation time 5?	   	tEXtSoftware ]p?:   tEXtDisclaimer ????   tEXtWarning ???   tEXtSource ????   tEXtComment ????   tEXtTitle ???'  @IDAT8???=K?A?????#??*?Rhm-???????*M?????????|??$?&??}g??Y?i1 ????a.????q$?w??\?K?LK??H?hR??-?u!T?K?ME?j0??>???L?-??	?L??? d???FF?V?2jE?2??`?l?2y???????O;???7?3??????<?<???0?f??t?.__????RV:?.???????g??^????w??#z/????d|x?i??(?}??<????r????y?m??????9u??m2?w\??Rl??Wl?<h???o&????7????????[ ?.d6    IEND?B`?                                                                                                                                                                                                                                                                                                                                                                                                           images/meteorGrey_small1.png                                                                        000644  000765  000024  00000001245 14066014314 020742  0                                                                                                    ustar 00alejandroflores                 staff                           000000  000000                                                                                                                                                                         ?PNG

   IHDR         r??  3IDATx??V?QA%C0C0C??@,)\?En???CA?*)#0B0C???[??;30U]??3??????????K?D?|?8aM?G??Lf???Ev?,B?t?o?DR0DN??x0?)?X?d?E*?T???oyt??Vj??Mg?i?Z??L??Re??K=o?""? ~B$?FG&?x?B?=EBT??M?`?o????????M??n?
T%??????^?5yc??P
Xlv? M?`??4o??????n??j?'!(??Y?tey??<o?????????C?H?,o??????<w?{?+S=?-@
|?]0)???"V??jaB:A?
???F??T???]??*?P??4???\??T?
`??RW??V??PT?S??!?E???0e????<Z??K?|?R?I?Z=?????t?????X??(?`+c??:??7u????$?U???D?????XF?JT?H??p?"Zqi????gR???<??BS?p?+?u(Q? 	??)jPM?????z%t??n?B??????E8f??m?j3?$*28??M?_G s%Q??_???>?o   -tEXtSoftware by.blooddy.crypto.image.PNG24Encoder??    IEND?B`?                                                                                                                                                                                                                                                                                                                                                           images/meteorGrey_med1.png                                                                          000644  000765  000024  00000001706 14066014314 020401  0                                                                                                    ustar 00alejandroflores                 staff                           000000  000000                                                                                                                                                                         ?PNG

   IHDR   +   +   ?]q?  TIDATx??Y[RA?\?Kp	.?%??_ ?)LB?11?	? ?????\B?g*'??df??????PC?????{?&?S>/W?O]<_.>????R?v???f??w??bu?X?V?W??g???B?IfD??[ ???iV?wFx[Y7I??n?77??T?????""X?6?]??{<;??????Pm???nkw??t??[X(<Z*??????v$??p7Y?jd!/??????hk?????:?;?Nq??"??R?"??Vj'N?Y?????X?????&
0-????A???!???N^??4:????}?3?g?L??HM????w??6?Kn?D???F?t????|?&?dm1??S?}x?/??b??7cD]??nM??e?!OG??,????jQ{?0?.?"Y???YN?zb???1?p????????????j?N??8??XJ?N(?|???dj??'$?T?*G?}????_?"
?$?B?9???X?vU8??d??;a_H0JAR??$!?/H3 k?-?*) ?????	?????c???NcJ???#?Z??c#??m???EN?2??H???t?-??r?</s???????L???R ?YtXq??N??i? ?K/Hj{?8??1L??>R????$?????????l?"?hr"??A??R???}??$????Gl??5???h??|?P?????	???D??z?8??N??&r	?7??p???hN?t??{8Ad?!	??7???Eq???i??C?5?%??i??c????Hs???0i?;r???,??????L?CW&?&?u"s???p???pOeGY>?Ll??2Q??C<??????^?1???N?   -tEXtSoftware by.blooddy.crypto.image.PNG24Encoder??    IEND?B`?                                                          images/meteorGrey_big1.png                                                                          000644  000765  000024  00000003372 14066014314 020376  0                                                                                                    ustar 00alejandroflores                 staff                           000000  000000                                                                                                                                                                         ?PNG

   IHDR   e   T   ?Z??  ?IDATx???iR1???G??#x???K
gd_d?E`K)O?<G?c??xS?'?$y?$?3U??Rkz:??_??N1|^N???5gg?j????>???????n?-??????j????Y??????????x/????3??w?????????v?c^L??x-?Xc??:??SiQ`S?+a`????\yQ?w??X]?????`0V't?1B???R??c?.??:??%?]p?????BG??q????yl[g_?;??z??]??x????{~??x?#?????????LG??16?h??@???Yo???T?g??{ad???\?O?????7L3v????@??b?1?7O.b?vx???vx?t_?7??a,B??	???Ah??z??????3???K????=?L???!A`@??3E??!????)?8a???%?]o???[??;-1??5/c?????v? ???;??w?D??\-
???8????(????t???VA?????A?I?.?e?????k;?8???Z?sP?aQGv?q?K7????u?!??c????"??Nn??c??I?
?O??&??`?]:??"??Wy4SQ`??u}???K'????? ?(????1Bh??`???b?i???Q???v?C????:?]p5?cpTn?7k???a???z}-Q????)!cYP??S????n\??????(?j?UK?J?@Xu-??+y?*??-Q??i? ??0?1??.??
?I]/&5t??[?6/?0??.??]????a?%-s1?|???]??1 ??$??>??U;aD?A???&?*3'???j(B?Rr???????[?5St???}?'???'M?0.tqv*?l*]0b????@W?]+?V?$c/i?v??z??/I]?	]0/?T?K?1????[???????t???%???3???D?2}&>??z?D???IF?g???y?w_*^???,/?>?#?f?2?$3???.B???b????\??3?!>?R???`?A?????'?l???%6?($??35?T}??R*R/??? a?g?p?(?7??d7?G?K(??1/Tm?)??}\.??P'\??1??r?	 ?p?n?jw?%??/?|T?a?'Li??1y	H?F.?rA??E?S?J?(???-????$?E%??C????s???x,?%?Cq`?2_?D?;\Y???L??? ??u?V?i?;??K???*?J??w?z?,c+???CYH?!?T?F??T?0dV?;?R*??<?0??????;d?G+???????I?eB????
????'??QJ??Z??K|g?`?s?$-=o?T?:?u?|?tZz??!:?a?S*?yI?06?K???W:!ck?7G???:?x????$??#i??????/??-?SJE)=o??6??R????[??b{x8*? ?????K??>????u?Q^?!f;l=!"?Y2???{*??UT0\?A???XU?r?s?'D40d?|??`?????c0?l??YI??????4?"????Y??;??"
<%m\x?n0?*??????:?j\4??0??9?'M.?X???Se?b??H??S?x????JFS?x???,#????a?	????~?tL2??6r?'???E????y?Nw???%|?????   -tEXtSoftware by.blooddy.crypto.image.PNG24Encoder??    IEND?B`?                                                                                                                                                                                                                                                                      images/playerShip1_orange.png                                                                       000644  000765  000024  00000005022 14066014314 021100  0                                                                                                    ustar 00alejandroflores                 staff                           000000  000000                                                                                                                                                                         ?PNG

   IHDR   c   K   d?9?  	?IDATx??][lU|??	/(??????G(??????b?????B?4??/??1^K4?????F."-,`)??Zj??m??-%P(`|>?7?z?tfv????s??!a??????_???2Zmm?????`}}=s*j?Puuu?"?od???"Q??UTTL&P????X?/??hzl?b fss?+2???V???0[[[]??~??*_????B????????????y???Q(????????e?n????D???4?>{RW?^e??_wD?G?a???VWW70???\??~?QI4=6???r??#2?<????>E"??[???2?????rk{zz???y?Vu
$?>??????????????"rkjGG?#2?<?I??g?????~????TT??>???7nx"??{??[;88?????[??Hd6? ???I?i??~??q?{?S?100????c?Q??b??&??"??????[??????@???8?????u????to} ??Z?dH??'??D\??~bq???4?!??m??~?{?nUy???????n???7=????{{b?'A?r??{???`f?loV?X???T?????_[C-;?a%?????P??ir??????*8? 	R?????????|%?a???<)A????dM?.J"p???fU+?Y??6Ps?S?'~?b|??????/??$A?"?Y??f????h`?v??J????|?W'%+5??c????p??????9???y??
B^P4?D??X????b~?C'e??	?H?d??(if?.,J-"??eX??4???\??Kt ?|b????<47???`]??'?7?3a^?f??(K?Q??gYKI???.??t?????{?u ???=???4???????K?=?T&\[(?#]?n \%E?'???BS^?Ay??@F??????N?lI??D'V???U ??L?=?rU??0??4?????????]??*?Ti???F2:?_+?kYMU?c?>Wk ?~?????????????aTvT????u?????9i???\? ??b????????>? ????_?(???=???M?R?DF?? ?S?k??????e???v?5zR?.5?pK????:??(?f$?F?????g\?/a?y2
E??Z??-o?NX???<?.}q6kY????v?k??R}?2????nE?????=?'?] ?|??.ThI??G?????'s?|?.^?.?I??[#0??A???{???\Wk??????hvS???-?????????????a??x4?Y??E??ZxC^???Y?^w??{?T??F/?y??;?ZZ??#??????O?,hs+b??|?!??^???????????x?);24????`X?? A???j???+c?????O?2????ujO?%;?~?$?(?A??=k32?^?Y????!????B???50>?_87?W}D7???Q??b?w????1??Z?????1"??Y??H2???O$??$?'????{b?!?H.?7?$?V??$#?d>1?+?2GV??$#?d?
??j[%?'???,??G??rS?2?e!?4???????6???)???Ic??????;HK?'2?????/????x$J?i?g??#?g?6x?>M?`?{b}_>?:?x?????+??}???~E?*??"??????@/?=?/?&?G?d?|v?F??X????? a?An????z?E>|R{{?_??z,?h?>??z?????cxc@[w??S4=D?D??? ???6??"????/?"d?'d?[5i?3????????]x???g?-?6?ut???.?O\3?pCp?bk?If??1???????i%??g????|!C|??% "?n? ^?M??Wq??d??~|???M???cD~6'M;?m??"??x ?C$?1,p?k?l???~mmm#%?|u?p?{`?Tv?;??????Mb?G'M(2?/?n??h8 ?V?/x?jB?k???W??oZ??(?D?=?T?(?
????/?^?x&???zA?3??p>fU???????????Jv?v???%X?C1%R?g?W?N(l(to?????ua}X'?k????U????
?????(W??j.O?*!+? ?6??~~a??u????B(?d`|???P?Q????n}n?????????O|???,V?U??x?????????????d???q???}?~\5tp????W????O?3>-??2???|JC`m_??L?x?;??@??????q??]?D??Q??N?i??H?z1??{?{z?<$???c??d??n?0l??a??)??????N?9?G???????_??I???m??)?????????xWQ7????-???Co?&??#<???]?lrfnD?>?tm??L??????V?M$B38   -tEXtSoftware by.blooddy.crypto.image.PNG24Encoder??    IEND?B`?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              