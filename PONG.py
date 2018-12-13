
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

white = (255, 255, 255)

bat_y = 4
ball_position = [3,3]
ball_volocity = [1,1]

while True:
    def draw_bat():
        sense.set_pixel(0, bat_y, white)
        sense.set_pixel(0, bat_y + 1, white)
        sense.set_pixel(0, bat_y - 1, white) 

def move_up(event):
    global bat_y
    if event.action  == 'pressed' and bat_y >1:
        bat_y -= 1
        
move_up

sense.stick.direction_up = move_up




