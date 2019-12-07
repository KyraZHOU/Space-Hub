import pygame as pg
import math

pg.init()
window = pg.display.set_mode((800,800)) # size of the screen
pg.display.set_caption("The Solar System")

const_G = 6.67*10**(-11)
mass_sun = 2*10**(30) #kg
sun_x = 400
sun_y = 400
sun_r = 50
earth_x = 400
earth_y = 250
earth_r = 15

r = 150*10**9 #m
orb_r = 150
lin_v = 29000 #m/s
del_t = 100
angle = math.pi/4 #rad

ang_v = 7.29*(10**(-5)) #rad/s
lin_acc = r*(ang_v**2)-((const_G*mass_sun)/(r**2)) #m/s^2
ang_acc = -(2*lin_v*ang_v)/r #rad/s^2


# orbital list
orb_list = []


def update_ang_acc(angular_v,del_t):
	angular_acc = angular_v/del_t
	return angular_acc

def update_lin_acc(angular_acc,radius):
	linear_acc = angular_acc*radius
	return linear_acc

def newVal(curVal,deltaT,derive):
	curVal = curVal + deltaT*derive
	return curVal

def update_linear(linear_speed,deltaT,linear_acc,linear_radius):
	linear_speed = newVal(linear_speed,deltaT,linear_acc)
	linear_radius = newVal(linear_radius,deltaT,linear_speed)
	return linear_speed,linear_radius

def update_angular(angular_speed,deltaT,angular_acc,angle_val):
	angular_speed = newVal(angular_speed,deltaT,angular_acc)
	angle_val = newVal(angle_val,deltaT,angular_speed)
	return angular_speed,angle_val 

def cur_pos(x,y,angle_val,orb_r):
	del_x = orb_r*(math.cos(angle_val))
	del_y = orb_r - orb_r*(math.sin(angle_val)) # the coordinates must be integers
	print("Angle:",angle)
	print("del_x & del_y:",del_x,del_y)
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
	print("x & y:",x,y)
	return x,y
'''
def update_pos(x,y,angle_val,orb_r):
	x = math.cos(angle_val) * orb_r + 400
	y = math.sin(-angle_val) * orb_r + 400
	print("Angle:",angle_val)
	return x,y
'''

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

	# update
	lin_acc = update_lin_acc(ang_v,del_t)
	ang_acc = update_ang_acc(ang_acc,r)
	lin_v,r = update_linear(lin_v,del_t,lin_acc,r)
	ang_v,angle = update_angular(ang_v,del_t,ang_acc,angle)

	print(lin_acc,ang_acc,lin_v,r,ang_v,angle)

	# draw the earth
	orb_r = r/(10**9)
	earth_x,earth_y = cur_pos(earth_x,earth_y,angle,orb_r) 
	pg.draw.circle(window,pg.Color("blue"),(int(round(earth_x,0)),int(round(earth_y,0))),earth_r,0)
	orb_list.append([earth_x,earth_y]) 

	# draw the orbital
	for i in range(0,len(orb_list)):
		pg.draw.rect(window,pg.Color("white"),(orb_list[i][0],orb_list[i][1],8,8),0)

	'''
	if len(orb_list) == 100:
		orb_list.pop(0)

	'''

	# update the screen
	pg.display.update()

pg.quit()
