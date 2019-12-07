import pygame as pg
import math

pg.init()
window = pg.display.set_mode((800,800)) # size of the screen
pg.display.set_caption("The Solar System")


sun_x = 400
sun_y = 400
sun_r = 50

# The size of the solar system radius
# Mercury: 2439.7 km -> 3
# Venus: 6051.8 km -> 6
# Earth: 6371 km -> 7
# Mars: 3389.5 km -> 4
# Jupiter: 69911 km -> 70
# Saturn: 58232 km -> 60
# Uranus: 25362 km -> 25
# Neptune: 24622 km ->  24
# SUN: 695,510 km
# 
# The distance of each planet to the sun
# Mercury: 57.9 Mkm -> 58
# Venus: 108.2 km -> 108
# Earth: 149.6 km -> 150
# Mars: 227.9 km -> 228
# Jupiter: 778.6 km -> 779
# Saturn: 1433.5 km -> 1434
# Uranus: 2872.5 km -> 2873
# Neptune: 4495.1 km ->  4495

count = 1

# text
# pg.font.init()
# font = pg.font.SysFont("Aerial",30,False,False) # Bold,Italics
# Text_Period = font.render("Orbital Period",True,(255,255,255)) # antialias - smooth curves
		

def cur_pos(x,y,p,orb_r):
	angle = count*(2*math.pi)/p # p = period
	del_x = orb_r*(math.sin(angle))
	del_y = orb_r - orb_r*(math.cos(angle)) # the coordinates must be integers

	if (x >= sun_x) and (y <= sun_y):
		x += del_x
		y += del_y
	elif (x >= sun_x) and (y >= sun_y):
		x -= del_x
		y += del_y
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

	# draw the mercury
	mercury_r = 7
	mercury_orb_r = 58 # orb_r + _y = sun_y
	mercury_x,mercury_y = cur_pos(400,342,88,mercury_orb_r) 
	pg.draw.circle(window,pg.Color("blue"),(int(round(mercury_x,0)),int(round(mercury_y,0))),mercury_r,0) 

	# draw the venus
	venus_r = 14
	venus_orb_r = 108 # p1_orb_r + p1_y = sun_y
	venus_x,venus_y = cur_pos(400,292,224,venus_orb_r)
	pg.draw.circle(window,pg.Color("purple"),(int(round(venus_x,0)),int(round(venus_y,0))),venus_r,0) 

	# draw the earth
	earth_r = 15
	earth_orb_r = 150 # earth_orb_r + earth_y = sun_y
	earth_x,earth_y = cur_pos(400,250,365,earth_orb_r) 
	pg.draw.circle(window,pg.Color("blue"),(int(round(earth_x,0)),int(round(earth_y,0))),earth_r,0) 

	# draw the mars
	mars_r = 9
	mars_orb_r = 228 # p2_orb_r + p2_y = sun_y
	mars_x,mars_y = cur_pos(400,172,687,mars_orb_r)
	pg.draw.circle(window,pg.Color("green"),(int(round(mars_x,0)),int(round(mars_y,0))),mars_r,0) 

	# draw the jupiter
	jupiter_r = 30
	jupiter_orb_r = 280 # p2_orb_r + p2_y = sun_y
	jupiter_x,jupiter_y = cur_pos(400,120,4331,jupiter_orb_r)
	pg.draw.circle(window,pg.Color("yellow"),(int(round(jupiter_x,0)),int(round(jupiter_y,0))),jupiter_r,0) 

	# draw the Saturn
	saturn_r = 25
	saturn_orb_r = 320 # p2_orb_r + p2_y = sun_y
	saturn_x,saturn_y = cur_pos(400,80,10747,saturn_orb_r)
	pg.draw.circle(window,pg.Color("blue"),(int(round(saturn_x,0)),int(round(saturn_y,0))),saturn_r,0) 

	# draw the Uranius
	uranius_r = 12
	uranius_orb_r = 350 # p2_orb_r + p2_y = sun_y
	uranius_x,uranius_y = cur_pos(400,50,30589,uranius_orb_r)
	pg.draw.circle(window,pg.Color("green"),(int(round(uranius_x,0)),int(round(uranius_y,0))),uranius_r,0) 
	
	# draw the Neptune
	neptune_r = 10
	neptune_orb_r = 380 # p2_orb_r + p2_y = sun_y
	neptune_x,neptune_y = cur_pos(400,20,59800,neptune_orb_r)
	pg.draw.circle(window,pg.Color("orange"),(int(round(neptune_x,0)),int(round(neptune_y,0))),neptune_r,0) 

	# draw the orbital
	pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),earth_orb_r,1)
	pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),mercury_orb_r,1) 
	pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),venus_orb_r,1)
	pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),mars_orb_r,1)
	pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),jupiter_orb_r,1) 
	pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),saturn_orb_r,1)
	pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),uranius_orb_r,1)
	pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),neptune_orb_r,1)

	# increment the count value
	count += 1

	# update the screen
	pg.display.update()

pg.quit()
