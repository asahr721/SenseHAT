
from sense_hat import SenseHat

sense = SenseHat()

r = 255
g = 255
b = 255
sense.clear((r, g, b))
sense.clear()
sense.set_pixel(0, 0, 255, 0, 0)
sense.set_pixel(0, 7, 0, 255, 0)
sense.set_pixel(7, 0, 0, 0, 255)
sense.set_pixel(7, 7, 255, 0, 255)
white = (255, 255, 255)
bat_y = 4
def draw_bat():
	sense.set_pixel(0, bat_y, white)
	sense.set_pixel(0, bat_y + 1, white)
	sense.set_pixel(0, bat_y - 1, white)
	
def move_up (event):
	global bat_y
	if event.action == 'pressed' and bat_y > 1:bat_y > 1
	bat_y -= 1
