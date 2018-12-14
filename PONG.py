
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

white = (255, 255, 255)

bat_y = 4
ball_position = [3,3]
ball_velocity = [1,1]


def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white) 

def move_up():
    global bat_y
    if event.action  == 'pressed' and bat_y > 1:
        bat_y -= 1
    
while True:
    sense.clear(0, 0, 0)
    draw_bat()
    sense.stick.direction_up = move_up()




