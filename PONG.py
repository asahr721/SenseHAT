from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

bat_y = 4 
ball_position = [3, 3]
ball_veloctiy = [1, 1]
score = 0

#Functions
def draw_bat():
  sense.set_pixel(0, bat_y, WHITE)
  sense.set_pixel(0, bat_y + 1, WHITE)
  sense.set_pixel(0, bat_y - 1, WHITE)
  
def move_up(event):
  global bat_y
  if event.action == 'pressed' and bat_y > 1:
    bat_y -= 1
    
def move_down(event):
  global bat_y
  if event.action == 'pressed' and bat_y < 6:
    bat_y += 1
  
def draw_ball():
  sense.set_pixel(ball_position[0], ball_position[1], BLUE)
  ball_position[0] += ball_veloctiy[0]
  if ball_position[0] == 7 or ball_position[0] == 0:
    ball_veloctiy[0] = -ball_veloctiy[0]
  ball_position[1] += ball_veloctiy[1]
  if ball_position[1] == 7 or ball_position[1] == 0:
    ball_veloctiy[1] = -ball_veloctiy[1]
  if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y +1):
    ball_veloctiy[0] = -ball_veloctiy[0]
  if ball_position[0] == 0:
    sense.show_message("You Lose")
  
#Main Program
while True:
  draw_bat()
  draw_ball()
  sleep(0.25)
  sense.stick.direction_up = move_up
  sense.stick.direction_down = move_down
  sense.clear(0, 0, 0)