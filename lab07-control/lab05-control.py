import arcade
import PlayaFunciones as playa


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02


#class Ball:
#    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
#
#        # Take the parameters of the init function above,
#        # and create instance variables out of them.
#        self.position_x = position_x
#        self.position_y = position_y
#        self.change_x = change_x
#        self.change_y = change_y
#        self.radius = radius
#        self.color = color
#
#    def draw(self):
#        """ Draw the balls with the instance variables we have. """
#        arcade.draw_circle_filled(self.position_x,
#                                  self.position_y,
#                                  self.radius,
#                                  self.color)
#
#    def update(self):
#        # Move the ball
#        self.position_y += self.change_y
#        self.position_x += self.change_x
#
#        # See if the ball hit the edge of the screen. If so, change direction
#        if self.position_x < self.radius:
#            self.position_x = self.radius
#
#        if self.position_x > SCREEN_WIDTH - self.radius:
#            self.position_x = SCREEN_WIDTH - self.radius
#
#        if self.position_y < self.radius:
#            self.position_y = self.radius
#
#        if self.position_y > SCREEN_HEIGHT - self.radius:
#            self.position_y = SCREEN_HEIGHT - self.radius

class Cangrejo:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the cangrejo the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, 30, arcade.color.RED)
        arcade.draw_line(start_x=self.position_x - 12, start_y=self.position_y + 20, end_x=self.position_x - 12, end_y=self.position_y + 50, color=arcade.color.RED,
                         line_width=5)  # Palito de ojo izquierda
        arcade.draw_line(start_x=self.position_x + 12, start_y=self.position_y + 20, end_x=self.position_x + 12, end_y=self.position_y + 50, color=arcade.color.RED,
                         line_width=5)  # Palito de ojo derecha
        arcade.draw_circle_filled(self.position_x - 12, self.position_y + 65, 15, arcade.color.WHITE)  # ojo derecho
        arcade.draw_circle_filled(self.position_x - 12, self.position_y + 65, 6, arcade.color.BLACK)  # ojo derecho por dentro
        arcade.draw_circle_filled(self.position_x + 12, self.position_y + 65, 15, arcade.color.WHITE)  # ojo izquierdo
        arcade.draw_circle_filled(self.position_x + 12, self.position_y + 65, 6, arcade.color.BLACK)  # ojo izquierdo por dentro
        arcade.draw_line(start_x=self.position_x - 20, start_y=self.position_y - 10, end_x=self.position_x - 25, end_y=self.position_y - 40, color=arcade.color.RED,
                         line_width=5)  # Patita 1/4
        arcade.draw_line(start_x=self.position_x - 27, start_y=self.position_y - 10, end_x=self.position_x - 37, end_y=self.position_y - 25, color=arcade.color.RED,
                         line_width=5)  # Patita 2/4
        arcade.draw_line(start_x=self.position_x + 20, start_y=self.position_y - 10, end_x=self.position_x + 25, end_y=self.position_y - 40, color=arcade.color.RED,
                         line_width=5)  # Patita 3/4
        arcade.draw_line(start_x=self.position_x + 27, start_y=self.position_y - 10, end_x=self.position_x + 37, end_y=self.position_y - 25, color=arcade.color.RED,
                         line_width=5)  # Patita 4/4

    def update(self):
        # Move the cangrejo
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the cangrejo hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
class Cangrejo:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the cangrejo the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, 30, arcade.color.RED)
        arcade.draw_line(start_x=self.position_x - 12, start_y=self.position_y + 20, end_x=self.position_x - 12, end_y=self.position_y + 50, color=arcade.color.RED,
                         line_width=5)  # Palito de ojo izquierda
        arcade.draw_line(start_x=self.position_x + 12, start_y=self.position_y + 20, end_x=self.position_x + 12, end_y=self.position_y + 50, color=arcade.color.RED,
                         line_width=5)  # Palito de ojo derecha
        arcade.draw_circle_filled(self.position_x - 12, self.position_y + 65, 15, arcade.color.WHITE)  # ojo derecho
        arcade.draw_circle_filled(self.position_x - 12, self.position_y + 65, 6, arcade.color.BLACK)  # ojo derecho por dentro
        arcade.draw_circle_filled(self.position_x + 12, self.position_y + 65, 15, arcade.color.WHITE)  # ojo izquierdo
        arcade.draw_circle_filled(self.position_x + 12, self.position_y + 65, 6, arcade.color.BLACK)  # ojo izquierdo por dentro
        arcade.draw_line(start_x=self.position_x - 20, start_y=self.position_y - 10, end_x=self.position_x - 25, end_y=self.position_y - 40, color=arcade.color.RED,
                         line_width=5)  # Patita 1/4
        arcade.draw_line(start_x=self.position_x - 27, start_y=self.position_y - 10, end_x=self.position_x - 37, end_y=self.position_y - 25, color=arcade.color.RED,
                         line_width=5)  # Patita 2/4
        arcade.draw_line(start_x=self.position_x + 20, start_y=self.position_y - 10, end_x=self.position_x + 25, end_y=self.position_y - 40, color=arcade.color.RED,
                         line_width=5)  # Patita 3/4
        arcade.draw_line(start_x=self.position_x + 27, start_y=self.position_y - 10, end_x=self.position_x + 37, end_y=self.position_y - 25, color=arcade.color.RED,
                         line_width=5)  # Patita 4/4

    def update(self):
        # Move the cangrejo
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the cangrejo hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        self.cangrejo = Cangrejo(500, 300, 0, 0, 30, arcade.color.RED)

        # Get a list of all the game controllers that are plugged in
        joysticks = arcade.get_joysticks()

        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

    def on_draw(self):

        """ Called whenever we need to draw the window. """
        arcade.start_render()
        playa.draw_land()
        playa.draw_sea()
        playa.draw_puesto_de_socorrista(190, 130)
        playa.draw_sol(500, 500)
        self.cangrejo.draw()
#        self.ball.draw()

    def update(self, delta_time):

        # Update the position according to the game controller
        if self.joystick:

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.cangrejo.change_x = 0
            else:
                self.cangrejo.change_x = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.cangrejo.change_y = 0
            else:
                self.cangrejo.change_y = -self.joystick.y * MOVEMENT_SPEED

        self.cangrejo.update()


def main():
    window = MyGame(800, 600, "Drawing Example")
    arcade.run()


main()