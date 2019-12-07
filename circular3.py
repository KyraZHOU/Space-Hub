import pygame as pg
import math

pg.init()
window = pg.display.set_mode((800,800)) # size of the screen
pg.display.set_caption("The Solar System")

sun_x = 400
sun_y = 400
sun_r = 50
mass_sun = 2*10**(30)
const_G = 6.67*10**(-11)
earth_r = 15
earth_orb_r = 150 # 150*10^6 km
earth_period = 365 

count = 1

# slider
slider_x = 30
value_x = math.sqrt(const_G*mass_sun/(earth_orb_r*10**9)) * 10**(-3)
max_v = (math.sqrt(const_G*mass_sun/(earth_orb_r*10**9)) * 2)*10**(-3) # 59479.1392 m/s = 60 km/s
min_v = (math.sqrt(const_G*mass_sun/(earth_orb_r*10**9)) * 1/2)*10**(-3) # 14869.7848 m/s = 15 km/s

slider2_x = 290
max_radius = ((const_G*mass_sun)/(max_v*10**(3))**2)*10**(-9) # convert into km
min_radius = ((const_G*mass_sun)/(min_v*10**(3))**2)*10**(-9) # convert into km

slider3_x = 550
slider_length = 200

# orbital list
orb_list = []

# text
pg.font.init()
font = pg.font.SysFont("Aerial",25,False,False) # Bold,Italics

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
		if pg.mouse.get_pressed()[0]:
			if (pg.mouse.get_pos()[0] >= 20) and (pg.mouse.get_pos()[0] <= 30 + slider_length):
				if (pg.mouse.get_pos()[1] >= 45) and (pg.mouse.get_pos()[1] <= 65):
					slider_x = pg.mouse.get_pos()[0]
			if (pg.mouse.get_pos()[0] >= 280) and (pg.mouse.get_pos()[0] <= 290 + slider_length):
				if (pg.mouse.get_pos()[1] >= 45) and (pg.mouse.get_pos()[1] <= 65):
					slider2_x = pg.mouse.get_pos()[0]
			if (pg.mouse.get_pos()[0] >= 540) and (pg.mouse.get_pos()[1] <= 550 + slider_length):
				if (pg.mouse.get_pos()[1] >= 45) and (pg.mouse.get_pos()[1] <= 65):
					slider3_x = pg.mouse.get_pos()[0]


	window.fill((0,0,0))

	# initialise acceleration
	angular_acc = value_x**2/earth_orb_r 

	# draw the sun
	pg.draw.circle(window,pg.Color("red"),(sun_x,sun_y),sun_r,0) 

	# draw the earth
	earth_x,earth_y = cur_pos(sun_x,sun_y-earth_orb_r,earth_period,earth_orb_r) 
	# print(earth_x,earth_y)
	# print(earth_orb_r)
	pg.draw.circle(window,pg.Color("blue"),(int(round(earth_x,0)),int(round(earth_y,0))),earth_r,0)
	orb_list.append([earth_x,earth_y]) 

	# increment the count value
	count += 1

	# draw the orbital
	# pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),earth_orb_r,1) # permanent orbital
	for i in range(0,len(orb_list)):
		pg.draw.rect(window,pg.Color("white"),(orb_list[i][0],orb_list[i][1],8,8),0)

	if len(orb_list) == 100:
		orb_list.pop(0)

	# draw the text
	pg.draw.rect(window,pg.Color("white"),(15,15,240,60),0)
	text_v = font.render("Orbital Veclocity: "+str(round(value_x,2)) + " km/s",True,(0,0,0)) # antialias - smooth curves
	window.blit(text_v,(20,20))
	pg.draw.rect(window,pg.Color("white"),(275,15,240,60),0)
	text_r = font.render("Orbital radius: " + str(round(earth_orb_r,1)) + " km",True,(0,0,0))
	window.blit(text_r,(280,20))
	pg.draw.rect(window,pg.Color("white"),(535,15,240,60),0)
	text_p = font.render("Orbital period: " + str(round(earth_period,0)) + " days",True,(0,0,0))
	window.blit(text_p,(540,20))

	# relationship between the velocity and radius
	value_x = (((slider_x-28 ) * max_v)  / slider_length) + min_v
	earth_orb_r = round((((const_G*mass_sun)/((value_x*10**3)**2))*10**(-9)),2)
	slider2_x = (((earth_orb_r - min_radius) /(max_radius-min_radius))*slider_length)+300

	# relationship between the radius and period
	# earth_period = math.sqrt((earth_orb_r**3)*4*(math.pi**2)/ (const_G*mass_sun))

	# draw the scale
	pg.draw.rect(window,pg.Color("gray"),(30,55,slider_length,10),0)
	pg.draw.circle(window,pg.Color("black"),(slider_x,60),10,0)

	pg.draw.rect(window,pg.Color("gray"),(290,55,slider_length,10),0)
	pg.draw.circle(window,pg.Color("black"),(int(slider2_x),60),10,0)

	pg.draw.rect(window,pg.Color("gray"),(550,55,slider_length,10),0)
	pg.draw.circle(window,pg.Color("black"),(slider3_x,60),10,0)

	# update the screen
	pg.display.update()

pg.quit()
