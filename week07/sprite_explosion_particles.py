  1"""
  2Sprite Explosion
  3
  4Simple program to show creating explosions with particles
  5
  6Artwork from http://kenney.nl
  7
  8If Python and Arcade are installed, this example can be run from the command line with:
  9python -m arcade.examples.sprite_explosion_particles
 10"""
 11import random
 12import math
 13import arcade
 14
 15SPRITE_SCALING_PLAYER = 0.5
 16SPRITE_SCALING_COIN = 0.3
 17SPRITE_SCALING_LASER = 0.8
 18COIN_COUNT = 50
 19
 20SCREEN_WIDTH = 800
 21SCREEN_HEIGHT = 600
 22SCREEN_TITLE = "Sprite Explosion Example"
 23
 24BULLET_SPEED = 5
 25
 26# --- Explosion Particles Related
 27
 28# How fast the particle will accelerate down. Make 0 if not desired
 29PARTICLE_GRAVITY = 0.05
 30
 31# How fast to fade the particle
 32PARTICLE_FADE_RATE = 8
 33
 34# How fast the particle moves. Range is from 2.5 <--> 5 with 2.5 and 2.5 set.
 35PARTICLE_MIN_SPEED = 2.5
 36PARTICLE_SPEED_RANGE = 2.5
 37
 38# How many particles per explosion
 39PARTICLE_COUNT = 20
 40
 41# How big the particle
 42PARTICLE_RADIUS = 3
 43
 44# Possible particle colors
 45PARTICLE_COLORS = [arcade.color.ALIZARIN_CRIMSON,
 46                   arcade.color.COQUELICOT,
 47                   arcade.color.LAVA,
 48                   arcade.color.KU_CRIMSON,
 49                   arcade.color.DARK_TANGERINE]
 50
 51# Chance we'll flip the texture to white and make it 'sparkle'
 52PARTICLE_SPARKLE_CHANCE = 0.02
 53
 54# --- Smoke
 55# Note: Adding smoke trails makes for a lot of sprites and can slow things
 56# down. If you want a lot, it will be necessary to move processing to GPU
 57# using transform feedback. If to slow, just get rid of smoke.
 58
 59# Start scale of smoke, and how fast is scales up
 60SMOKE_START_SCALE = 0.25
 61SMOKE_EXPANSION_RATE = 0.03
 62
 63# Rate smoke fades, and rises
 64SMOKE_FADE_RATE = 7
 65SMOKE_RISE_RATE = 0.5
 66
 67# Chance we leave smoke trail
 68SMOKE_CHANCE = 0.25
 69
 70class Smoke(arcade.SpriteCircle):
 71    """ This represents a puff of smoke """
 72    def __init__(self, size):
 73        super().__init__(size, arcade.color.LIGHT_GRAY, soft=True)
 74        self.change_y = SMOKE_RISE_RATE
 75        self.scale = SMOKE_START_SCALE
 76
 77    def update(self):
 78        """ Update this particle """
 79        if self.alpha <= PARTICLE_FADE_RATE:
 80            # Remove faded out particles
 81            self.remove_from_sprite_lists()
 82        else:
 83            # Update values
 84            self.alpha -= SMOKE_FADE_RATE
 85            self.center_x += self.change_x
 86            self.center_y += self.change_y
 87            self.scale += SMOKE_EXPANSION_RATE
 88
 89
 90class Particle(arcade.SpriteCircle):
 91    """ Explosion particle """
 92    def __init__(self, my_list):
 93        # Choose a random color
 94        color = random.choice(PARTICLE_COLORS)
 95
 96        # Make the particle
 97        super().__init__(PARTICLE_RADIUS, color)
 98
 99        # Track normal particle texture, so we can 'flip' when we sparkle.
100        self.normal_texture = self.texture
101
102        # Keep track of the list we are in, so we can add a smoke trail
103        self.my_list = my_list
104
105        # Set direction/speed
106        speed = random.random() * PARTICLE_SPEED_RANGE + PARTICLE_MIN_SPEED
107        direction = random.randrange(360)
108        self.change_x = math.sin(math.radians(direction)) * speed
109        self.change_y = math.cos(math.radians(direction)) * speed
110
111        # Track original alpha. Used as part of 'sparkle' where we temp set the
112        # alpha back to 255
113        self.my_alpha = 255
114
115        # What list do we add smoke particles to?
116        self.my_list = my_list
117
118    def update(self):
119        """ Update the particle """
120        if self.my_alpha <= PARTICLE_FADE_RATE:
121            # Faded out, remove
122            self.remove_from_sprite_lists()
123        else:
124            # Update
125            self.my_alpha -= PARTICLE_FADE_RATE
126            self.alpha = self.my_alpha
127            self.center_x += self.change_x
128            self.center_y += self.change_y
129            self.change_y -= PARTICLE_GRAVITY
130
131            # Should we sparkle this?
132            if random.random() <= PARTICLE_SPARKLE_CHANCE:
133                self.alpha = 255
134                self.texture = arcade.make_circle_texture(self.width, arcade.color.WHITE)
135            else:
136                self.texture = self.normal_texture
137
138            # Leave a smoke particle?
139            if random.random() <= SMOKE_CHANCE:
140                smoke = Smoke(5)
141                smoke.position = self.position
142                self.my_list.append(smoke)
143
144
145class MyGame(arcade.Window):
146    """ Main application class. """
147
148    def __init__(self):
149        """ Initializer """
150        # Call the parent class initializer
151        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
152
153        # Variables that will hold sprite lists
154        self.player_list = None
155        self.coin_list = None
156        self.bullet_list = None
157        self.explosions_list = None
158
159        # Set up the player info
160        self.player_sprite = None
161        self.score = 0
162
163        # Don't show the mouse cursor
164        self.set_mouse_visible(False)
165
166        # Load sounds. Sounds from kenney.nl
167        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
168        self.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")
169
170        arcade.set_background_color(arcade.color.BLACK)
171
172    def setup(self):
173
174        """ Set up the game and initialize the variables. """
175
176        # Sprite lists
177        self.player_list = arcade.SpriteList()
178        self.coin_list = arcade.SpriteList()
179        self.bullet_list = arcade.SpriteList()
180        self.explosions_list = arcade.SpriteList()
181
182        # Set up the player
183        self.score = 0
184
185        # Image from kenney.nl
186        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip2_orange.png", SPRITE_SCALING_PLAYER)
187        self.player_sprite.center_x = 50
188        self.player_sprite.center_y = 70
189        self.player_list.append(self.player_sprite)
190
191        # Create the coins
192        for coin_index in range(COIN_COUNT):
193
194            # Create the coin instance
195            # Coin image from kenney.nl
196            coin = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", SPRITE_SCALING_COIN)
197            coin.angle = 180
198
199            # Position the coin
200            coin.center_x = random.randrange(SCREEN_WIDTH)
201            coin.center_y = random.randrange(150, SCREEN_HEIGHT)
202
203            # Add the coin to the lists
204            self.coin_list.append(coin)
205
206    def on_draw(self):
207        """
208        Render the screen.
209        """
210
211        # This command has to happen before we start drawing
212        arcade.start_render()
213
214        # Draw all the sprites.
215        self.coin_list.draw()
216        self.bullet_list.draw()
217        self.player_list.draw()
218        self.explosions_list.draw()
219
220        # Render the text
221        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
222
223    def on_mouse_motion(self, x, y, dx, dy):
224        """
225        Called whenever the mouse moves.
226        """
227        self.player_sprite.center_x = x
228
229    def on_mouse_press(self, x, y, button, modifiers):
230        """
231        Called whenever the mouse button is clicked.
232        """
233
234        # Gunshot sound
235        arcade.sound.play_sound(self.gun_sound)
236
237        # Create a bullet
238        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)
239
240        # The image points to the right, and we want it to point up. So
241        # rotate it.
242        bullet.angle = 90
243
244        # Give it a speed
245        bullet.change_y = BULLET_SPEED
246
247        # Position the bullet
248        bullet.center_x = self.player_sprite.center_x
249        bullet.bottom = self.player_sprite.top
250
251        # Add the bullet to the appropriate lists
252        self.bullet_list.append(bullet)
253
254    def on_update(self, delta_time):
255        """ Movement and game logic """
256
257        # Call update on bullet sprites
258        self.bullet_list.update()
259        self.explosions_list.update()
260
261        # Loop through each bullet
262        for bullet in self.bullet_list:
263
264            # Check this bullet to see if it hit a coin
265            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
266
267            # If it did...
268            if len(hit_list) > 0:
269
270                # Get rid of the bullet
271                bullet.remove_from_sprite_lists()
272
273            # For every coin we hit, add to the score and remove the coin
274            for coin in hit_list:
275                # Make an explosion
276                for i in range(PARTICLE_COUNT):
277                    particle = Particle(self.explosions_list)
278                    particle.position = coin.position
279                    self.explosions_list.append(particle)
280
281                smoke = Smoke(50)
282                smoke.position = coin.position
283                self.explosions_list.append(smoke)
284
285                coin.remove_from_sprite_lists()
286                self.score += 1
287
288                # Hit Sound
289                arcade.sound.play_sound(self.hit_sound)
290
291            # If the bullet flies off-screen, remove it.
292            if bullet.bottom > SCREEN_HEIGHT:
293                bullet.remove_from_sprite_lists()
294
295
296def main():
297    window = MyGame()
298    window.center_window()
299    window.setup()
300    arcade.run()
301
302
303if __name__ == "__main__":
304    main()