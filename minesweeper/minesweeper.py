import arcade
from random import randint

arcade.open_window(800, 800, "Drawing Example")
arcade.set_background_color(arcade.color.GREEN_YELLOW)
arcade.start_render()

par = 1
for y in range (760,0,-80):
    if (par == 1):
        for x in range(40,800,160):
            arcade.draw_rectangle_filled(x,y, 80, 80, arcade.color.APPLE_GREEN)
    else:
        for x in range(120,800,160):
            arcade.draw_rectangle_filled(x,y, 80, 80, arcade.color.APPLE_GREEN)
    par = par * -1

for i in range (0,11):
    random_x = randint(1,10)
    random_y = randint(1,10)
    print (random_x , "x",random_y , "y")
    if (random_x % 2) == 0:
        random_x = random_x + 1
    if (random_y % 2) == 0:
        random_y = random_y + 1
    arcade.draw_circle_filled(random_x * 40,random_y * 40, 40, arcade.color.RED)

arcade.finish_render()
arcade.run()