""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.35
SPRITE_SCALING_GOOD_COIN = 0.05
SPRITE_SCALING_BAD_COIN = 0.02
GOOD_COIN_COUNT = 50
BAD_COIN_COUNT = 15

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.good_sprite_list = None
        self.bad_sprite_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("eminem.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(GOOD_COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            good_coin = arcade.Sprite("vinyl.png", SPRITE_SCALING_GOOD_COIN)

            # Position the coin
            good_coin.center_x = random.randrange(SCREEN_WIDTH)
            good_coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.good_sprite_list.append(good_coin)

        # Create the bad coins
        for i in range(BAD_COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            bad_coin = arcade.Sprite("red_x.png", SPRITE_SCALING_BAD_COIN)

            # Position the coin
            bad_coin.center_x = random.randrange(SCREEN_WIDTH)
            bad_coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.bad_sprite_list.append(bad_coin)
            #hit_list = arcade.check_for_collision_with_list(self.bad_sprite_list, self.good_sprite_list)
            #for bad_coin in hit_list:
            #    bad_coin.remove_from_sprite_lists()
            #    self.score += 1
            #    bad_coin.center_x = random.randrange(SCREEN_WIDTH)
            #    bad_coin.center_y = random.randrange(SCREEN_HEIGHT)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.good_sprite_list.draw()
        self.bad_sprite_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if len(self.good_sprite_list) == 0:
            self.set_mouse_visible(True)
            arcade.draw_rectangle_filled(400,300,800,600,arcade.color.AMAZON)
            arcade.draw_text("Bien hecho mi pana, tu score es: " + str(self.score), 190, 300, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.good_sprite_list.update()
        self.bad_sprite_list.update()

        # Generate a list of all sprites that collided with the player.
        #coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
        #                                                      self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        #for coin in coins_hit_list:
        #    coin.remove_from_sprite_lists()
        #    self.score += 1
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
        for good_sprite in hit_list:
            good_sprite.remove_from_sprite_lists()
            self.score += 1
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
        for bad_sprite in hit_list:
            bad_sprite.remove_from_sprite_lists()
            self.score -= 1
            bruh_effect = arcade.load_sound("bruh.mp3")
            arcade.play_sound(bruh_effect)

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()