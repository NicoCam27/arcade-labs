# Import the "arcade" library
import arcade

def draw_land():
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.YELLOW_ORANGE)

def draw_sea():
    arcade.draw_lrtb_rectangle_filled(0, 800, 310, 170, arcade.color.SEA_BLUE)

def draw_puesto_de_socorrista(x,y): # En el ejemplo: x = 190, y = 130
    arcade.draw_rectangle_filled(x, y, 70, 170, arcade.color.DARK_BROWN) # El tronco de puesto
    arcade.draw_rectangle_filled(x, y+80, 180, 15, arcade.color.DARK_BROWN) # El suelo del puesto
    arcade.draw_rectangle_filled(x - 15, y-5, 10, 195, arcade.color.BROWN) # Palo 1/2 de la escalera
    arcade.draw_rectangle_filled(x + 15, y-5, 10, 195, arcade.color.BROWN) # Palo 2/2 de la escalera
    arcade.draw_line(start_x = x - 15, start_y= y - 80, end_x = x + 15, end_y = y - 80, color=arcade.color.WOOD_BROWN, line_width=10) # Palito 1/9 de la escalera
    arcade.draw_line(start_x = x - 15, start_y= y - 60, end_x = x + 15, end_y = y - 60, color=arcade.color.WOOD_BROWN, line_width=10) # Palito 2/9 de la escalera
    arcade.draw_line(start_x = x - 15, start_y= y - 40, end_x = x + 15, end_y = y - 40, color=arcade.color.WOOD_BROWN, line_width=10) # Palito 3/9 de la escalera
    arcade.draw_line(start_x = x - 15, start_y= y - 20, end_x = x + 15, end_y = y - 20, color=arcade.color.WOOD_BROWN, line_width=10) # Palito 4/9 de la escalera
    arcade.draw_line(start_x = x - 15, start_y= y, end_x = x + 15, end_y = y, color=arcade.color.WOOD_BROWN, line_width=10) # Palito 5/9 de la escalera
    arcade.draw_line(start_x = x - 15, start_y= y + 20, end_x = x + 15, end_y = y + 20, color=arcade.color.WOOD_BROWN, line_width=10) # Palito 6/9 de la escalera
    arcade.draw_line(start_x = x - 15, start_y= y + 40, end_x = x + 15, end_y = y + 40, color=arcade.color.WOOD_BROWN, line_width=10) # Palito 7/9 de la escalera
    arcade.draw_line(start_x = x - 15, start_y= y + 60, end_x = x + 15, end_y = y + 60, color=arcade.color.WOOD_BROWN, line_width=10) # Palito 8/9 de la escalera
    arcade.draw_line(start_x = x - 15, start_y= y + 80, end_x= x + 15, end_y = y + 80, color=arcade.color.WOOD_BROWN, line_width=10) # Palito 9/9 de la escalera
    # #El paraguas
    arcade.draw_arc_filled(center_x= x, center_y=y+167, width=300, height=220, color=arcade.color.BROWN, start_angle=0, end_angle=180,tilt_angle=0) # Arco principal
    arcade.draw_arc_filled(center_x= x - 124, center_y=y+167, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0) # Arquito 1/6
    arcade.draw_arc_filled(center_x= x - 74, center_y=y+167, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0) # Arquito 2/6
    arcade.draw_arc_filled(center_x= x - 24, center_y=y+167, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0) # Arquito 3/6
    arcade.draw_arc_filled(center_x= x + 26, center_y=y+167, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0) # Arquito 4/6
    arcade.draw_arc_filled(center_x= x + 76, center_y=y+167, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0) # Arquito 5/6
    arcade.draw_arc_filled(center_x= x + 126, center_y=y+167, width=50, height=36.7, color=arcade.color.SEA_BLUE, start_angle=0, end_angle=180,tilt_angle=0) # Arquito 6/6
    # palo de paraguas de puesto de socorrista
    arcade.draw_line(start_x=x, start_y=y+85, end_x=x, end_y= y + 190, color=arcade.color.BROWN, line_width=10)

def draw_sol(x,y): # En este ejemplo x = 500, y = 500
    arcade.draw_circle_filled(x, y, 50, arcade.color.SUNGLOW)

def draw_cangrejo(x,y):
    arcade.draw_circle_filled(x,y,30, arcade.color.RED)
    arcade.draw_line(start_x = x - 12, start_y= y + 20, end_x = x - 12, end_y = y + 50, color=arcade.color.RED, line_width=5) # Palito de ojo izquierda
    arcade.draw_line(start_x = x + 12, start_y= y + 20, end_x = x + 12, end_y = y + 50, color=arcade.color.RED, line_width=5) # Palito de ojo derecha
    arcade.draw_circle_filled(x - 12, y + 65, 15, arcade.color.WHITE)  # ojo derecho
    arcade.draw_circle_filled(x - 12, y + 65, 6, arcade.color.BLACK)  # ojo derecho por dentro
    arcade.draw_circle_filled(x + 12, y + 65, 15, arcade.color.WHITE)  # ojo izquierdo
    arcade.draw_circle_filled(x + 12, y + 65, 6, arcade.color.BLACK)  # ojo izquierdo por dentro
    arcade.draw_line(start_x = x - 20, start_y= y - 10, end_x = x - 25, end_y = y - 40, color=arcade.color.RED, line_width=5) # Patita 1/4
    arcade.draw_line(start_x = x - 27, start_y= y - 10, end_x = x - 37, end_y = y - 25, color=arcade.color.RED, line_width=5) # Patita 2/4
    arcade.draw_line(start_x = x + 20, start_y= y - 10, end_x = x + 25, end_y = y - 40, color=arcade.color.RED, line_width=5) # Patita 3/4
    arcade.draw_line(start_x = x + 27, start_y= y - 10, end_x = x + 37, end_y = y - 25, color=arcade.color.RED, line_width=5) # Patita 4/4
