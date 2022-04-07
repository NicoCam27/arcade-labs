
import math
import random
import arcade
from typing import Optional
import time
import personaje # Aquí se importa la clase de personaje

from arcade.pymunk_physics_engine import PymunkPhysicsEngine

SCREEN_TITLE = "Juego de equipo Durum studio"
SPRITE_SCALING_PLAYER = 0.5
MOVEMENT_SPEED = 5

SPRITE_IMAGE_SIZE = 128
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

SCREEN_WIDTH = SPRITE_SIZE * 15
SCREEN_HEIGHT = SPRITE_SIZE * 10


PLAYER_MOVE_FORCE = 4000


class MyWindow(arcade.Window):
    """ Main Window """
    def __init__(self, width, height, title, protagonista):
        """ Init """
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)
        self.physics_engine: Optional[PymunkPhysicsEngine] = None
        self.personaje = protagonista

    def setup(self):
        """ Set up everything """


        # --- Pymunk Physics Engine Setup ---

        # The default damping for every object controls the percent of velocity
        # the object will keep each second. A value of 1.0 is no speed loss,
        # 0.9 is 10% per second, 0.1 is 90% per second.
        # For top-down games, this is basically the friction for moving objects.
        # For platformers with gravity, this should probably be set to 1.0.
        # Default value is 1.0 if not specified.
        damping = 0.7

        # Set the gravity. (0, 0) is good for outer space and top-down.
        gravity = (0, 0)

        # Create the physics engine
        self.physics_engine = PymunkPhysicsEngine(damping=damping,
                                                  gravity=gravity)

    def on_key_press(self, symbol: int, modifiers: int):
        self.personaje.on_key_press()

    def on_key_release(self, symbol: int, modifiers: int):
        self.personaje.on_key_release()

    def on_update(self, delta_time):
        """ Movement and game logic """
        # --- Move items in the physics engine
        self.physics_engine.step()
        self.personaje.on_update(delta_time)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.personaje.on_draw()

def main():
    """ Main method """
    juana = personaje.Protagonista(":resources:images/animated_characters/female_person/femalePerson_idle.png")
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, juana)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()