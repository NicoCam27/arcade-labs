"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# We draw the sand *****************
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.YELLOW_ORANGE)

# --- Draw the barn ---

# Barn cement base
arcade.draw_lrtb_rectangle_filled(0, 800, 310, 170, arcade.color.SEA_BLUE)

# Bottom half
# arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)

# Left-bottom window
# arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
# arcade.draw_rectangle_filled(70, 260, 20, 30, arcade.color.BLACK)

# Right-bottom window
# arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
# arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)


# Base del puesto de socorrista
arcade.draw_rectangle_filled(190, 130, 70, 170, arcade.color.DARK_BROWN)

# Draw 2nd level door ***************
arcade.draw_rectangle_outline(190, 255, 165, 80, arcade.color.DARK_BROWN, 5)

# El suelo del puesto de socorrista
arcade.draw_rectangle_filled(190, 210, 180, 15, arcade.color.DARK_BROWN) # Se dibuja antes para que sea más fácil implementar las escaleras

# La escalera
arcade.draw_rectangle_filled(175, 125, 10, 195, arcade.color.BROWN)
arcade.draw_rectangle_filled(205, 125, 10, 195, arcade.color.BROWN)

arcade.draw_line(start_x=175, start_y=50, end_x=205, end_y=50, color=arcade.color.WOOD_BROWN, line_width=10)
arcade.draw_line(start_x=175, start_y=70, end_x=205, end_y=70, color=arcade.color.WOOD_BROWN, line_width=10)
arcade.draw_line(start_x=175, start_y=90, end_x=205, end_y=90, color=arcade.color.WOOD_BROWN, line_width=10)
arcade.draw_line(start_x=175, start_y=110, end_x=205, end_y=110, color=arcade.color.WOOD_BROWN, line_width=10)
arcade.draw_line(start_x=175, start_y=130, end_x=205, end_y=130, color=arcade.color.WOOD_BROWN, line_width=10)
arcade.draw_line(start_x=175, start_y=150, end_x=205, end_y=150, color=arcade.color.WOOD_BROWN, line_width=10)
arcade.draw_line(start_x=175, start_y=170, end_x=205, end_y=170, color=arcade.color.WOOD_BROWN, line_width=10)
arcade.draw_line(start_x=175, start_y=190, end_x=205, end_y=190, color=arcade.color.WOOD_BROWN, line_width=10)
arcade.draw_line(start_x=175, start_y=210, end_x=205, end_y=210, color=arcade.color.WOOD_BROWN, line_width=10)



# Draw second level of barn
#arcade.draw_polygon_filled([[20, 297],
#                            [100, 370],
#                            [280, 370],
#                            [360, 297]],
#                            arcade.color.BROWN)




#El paraguas

arcade.draw_arc_filled(center_x=190, center_y=297, width=300, height=220, color=arcade.color.BROWN, start_angle=0, end_angle=180,tilt_angle=0)

arcade.draw_arc_filled(center_x=66, center_y=297, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0)

arcade.draw_arc_filled(center_x=116, center_y=297, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0)

arcade.draw_arc_filled(center_x=166, center_y=297, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0)

arcade.draw_arc_filled(center_x=216, center_y=297, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0)

arcade.draw_arc_filled(center_x=266, center_y=297, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0)

arcade.draw_arc_filled(center_x=316, center_y=297, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0)


# palo de paraguas de puesto de socorrista
arcade.draw_line(start_x=190, start_y=215, end_x=190, end_y=320, color=arcade.color.BROWN, line_width=10)

# Left-top window
# arcade.draw_rectangle_filled(130, 440, 30, 40, arcade.color.BONE)
# arcade.draw_rectangle_filled(130, 440, 20, 30, arcade.color.BLACK)

# Right-top window
# arcade.draw_rectangle_filled(250, 440, 30, 40, arcade.color.BONE)
# arcade.draw_rectangle_filled(250, 440, 20, 30, arcade.color.BLACK)


# --- Draw the tractor ---

# Draw the engine
#arcade.draw_rectangle_filled(600, 120, 140, 70, arcade.color.GRAY)
#arcade.draw_rectangle_filled(590, 105, 90, 40, arcade.color.BLACK)

# Draw the smoke stack
#arcade.draw_rectangle_filled(580, 175, 10, 40, arcade.color.BLACK)




arcade.draw_circle_filled(500, 500, 50, arcade.color.SUNGLOW)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

