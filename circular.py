import pygame as pg
import math

pg.init()
window = pg.display.set_mode((800,800)) # size of the screen
pg.display.set_caption("Circular Motion")


sun_x = 400
sun_y = 400
sun_r = 50
earth_x = 400
earth_y = 100
earth_r = 20
orb_r = 300

count = 1
period = 365

# text
# pg.font.init()
# font = pg.font.SysFont("Aerial",30,False,False) # Bold,Italics
# Text_Period = font.render("Orbital Period",True,(255,255,255)) # antialias - smooth curves
		

def cur_pos(x,y):
	angle = count*(2*math.pi)/period
	del_x = orb_r*(math.sin(angle))
	del_y = orb_r - orb_r*(math.cos(angle)) # the coordinates must be integers

	if (x >= sun_x) and (y <= sun_y):
		x += del_x
		y += del_y
	elif (x >= sun_x) and (y >= sun_y):
		x -= del_x
		earth_y += del_y
	elif (x <= sun_x) and (y >= sun_y):
		x-= del_x
		y -= del_y
	elif (x <= sun_x) and (y <= sun_y):
		x += del_x
		y -= del_y
	return x,y


run = True
while run:
	# delay for showing the slow motion 
	pg.time.delay(1)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

	window.fill((0,0,0))

	# draw the sun
	pg.draw.circle(window,pg.Color("red"),(sun_x,sun_y),sun_r,0) 

	# draw the earth
	earth_x,earth_y = cur_pos(400,100)
	pg.draw.circle(window,pg.Color("purple"),(int(round(earth_x,0)),int(round(earth_y))),earth_r,1) 
	count += 1
	# draw the orbital
	pg.draw.circle(window,pg.Color("red"),(sun_x,sun_y),orb_r,1) 
	pg.display.update()

pg.quit()
