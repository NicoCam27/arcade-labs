# Clase personaje (Clase Padre, deciende de la clase sprite)
# Que tenga getters y setters.
# Getters de posicion.
# Movimiento (W.A.S.D para el protagoinsta, y para los demás personajes su IA)

# Ataque (un metodo de ataque)
# Vida (Puntos de vida, cambios de animaciones al ser golpeado?)


# Clase Protagonista (Clase hija)
# Que tenga getters y setters.
# Getters de posicion.
# Que herede el movimiento.
# Ataque - puede tener varios tipos de movimientos.

# Clase enemigo (Clase hija).
# Eso ya es para adelante.


# Para el lunes, pantalla vacia con un sprite que se mueva bien

import arcade
from typing import Optional
from arcade.pymunk_physics_engine import PymunkPhysicsEngine

SPRITE_SCALING_PLAYER = 0.5
MOVEMENT_SPEED = 5

SPRITE_IMAGE_SIZE = 128
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

SCREEN_WIDTH = SPRITE_SIZE * 15
SCREEN_HEIGHT = SPRITE_SIZE * 10

# Physics force used to move the player. Higher number, faster accelerating.
PLAYER_MOVE_FORCE = 4000
BULLET_MOVE_FORCE = 2500

PLAYER_MOVE_FORCE = 4000


class Personaje(arcade.Sprite):

    def __init__(self, sprite):
        super().__init__()
        self.player_list = None
        self.player_sprite = arcade.Sprite(sprite, SPRITE_SCALING_PLAYER)
        self.hp = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)
        self.physics_engine.add_sprite(self.player_sprite,
                                       friction=0.6,
                                       moment=PymunkPhysicsEngine.MOMENT_INF,
                                       damping=0.0000001,
                                       collision_type="player",
                                       max_velocity=350)

    def get_hp(self):
        return self.hp

    def set_hp(self, new_hp):
        self.hp = new_hp

    #def movement(self):

    def draw_personaje(self):
        self.player_list.draw()

class Protagonista(Personaje):

    def __init__(self, sprite):
        super().__init__(sprite)
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.physics_engine: Optional[PymunkPhysicsEngine] = None
        self.player_list = None
        self.player_sprite = arcade.Sprite(sprite, SPRITE_SCALING_PLAYER)
        self.hp = None

    def setup(self):
        """ Set up everything """
        # Create the sprite lists
        self.player_list = arcade.SpriteList()
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)
        self.physics_engine.add_sprite(self.player_sprite,
                                       friction=0.6,
                                       moment=PymunkPhysicsEngine.MOMENT_INF,
                                       damping=0.0000001,
                                       collision_type="player",
                                       max_velocity=350)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False

    def on_update(self, delta_time):
      """ Movement """

      # Calculate speed based on the keys pressed
      self.player_sprite.change_x = 0
      self.player_sprite.change_y = 0

      if self.up_pressed and not self.down_pressed:
          force = (0, PLAYER_MOVE_FORCE)
          self.physics_engine.apply_force(self.player_sprite, force)
      elif self.down_pressed and not self.up_pressed:
          force = (0, -PLAYER_MOVE_FORCE)
          self.physics_engine.apply_force(self.player_sprite, force)
      if self.left_pressed and not self.right_pressed:
          self.player_sprite.change_x = -MOVEMENT_SPEED
          force = (-PLAYER_MOVE_FORCE, 0)
          self.physics_engine.apply_force(self.player_sprite, force)
      elif self.right_pressed and not self.left_pressed:
          force = (PLAYER_MOVE_FORCE, 0)
          self.physics_engine.apply_force(self.player_sprite, force)

      # --- Move items in the physics engine
      self.physics_engine.step()

    def on_draw(self):
       """ Draw everything """
       arcade.start_render()
       self.player_list.draw()

   #def update_protagonista(self):
   #    # Calculate speed based on the keys pressed
   #    self.player_sprite.change_x = 0
   #    self.player_sprite.change_y = 0

   #    if self.up_pressed and not self.down_pressed:
   #        force = (0, PLAYER_MOVE_FORCE)
   #        self.physics_engine.apply_force(self.player_sprite, force)
   #    elif self.down_pressed and not self.up_pressed:
   #        force = (0, -PLAYER_MOVE_FORCE)
   #        self.physics_engine.apply_force(self.player_sprite, force)
   #    if self.left_pressed and not self.right_pressed:
   #        self.player_sprite.change_x = -MOVEMENT_SPEED
   #        force = (-PLAYER_MOVE_FORCE, 0)
   #        self.physics_engine.apply_force(self.player_sprite, force)
   #    elif self.right_pressed and not self.left_pressed:
   #        force = (PLAYER_MOVE_FORCE, 0)
   #        self.physics_engine.apply_force(self.player_sprite, force)

   #    # --- Move items in the physics engine
   #    #self.physics_engine.step()


   #def draw_protagonista(self):
   #    self.player_list.draw()

# --- Pymunk Physics Engine Setup ---

# The default damping for every object controls the percent of velocity
# the object will keep each second. A value of 1.0 is no speed loss,
# 0.9 is 10% per second, 0.1 is 90% per second.
# For top-down games, this is basically the friction for moving objects.
# For platformers with gravity, this should probably be set to 1.0.
# Default value is 1.0 if not specified.
# damping = 0.7

# Set the gravity. (0, 0) is good for outer space and top-down.
# gravity = (0, 0)

# Create the physics engine
# self.physics_engine = PymunkPhysicsEngine(damping=damping,gravity=gravity)
