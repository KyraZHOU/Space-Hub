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

r = 150*10**9  # AU
orb_r = r/(10**9)
lin_v = 0 #m/s
angle = math.pi/2 #rad
ang_v = 2*10**(-7)#rad/s
lin_acc = r*(ang_v**2)-((const_G*mass_sun)/(r**2)) #m/s^2
ang_acc = -(2*lin_v*ang_v)/r #rad/s^2
planet_v = math.sqrt(const_G*mass_sun/(r)) * 10**(-3)

# orbital list
orb_list = []

num_cal_frame = 10
del_t = 3600*24/num_cal_frame

def update_lin_acc(radius,angular_v):
	linear_acc = radius*(angular_v**2)-((const_G*mass_sun)/(radius**2))
	return linear_acc

def update_ang_acc(linear_v,angular_v,radius):
	angular_acc = -(2*linear_v*angular_v)/radius
	return angular_acc

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

def update_pos(x,y,angle_val,orb_r):
	x = math.cos(angle_val) * orb_r + 400
	y = math.sin(-angle_val) * orb_r + 400
	print("Angle:",angle_val)
	return x,y


def full_update(linear_acc,angular_acc,radius,linear_speed,angular_speed,angle_val,deltaT):
	# update
	linear_acc = update_lin_acc(radius,angular_speed)
	angular_acc = update_ang_acc(linear_speed,angular_speed,radius)
	linear_speed,radius = update_linear(linear_speed,deltaT,linear_acc,radius)
	angular_speed,angle_val = update_angular(angular_speed,deltaT,angular_acc,angle_val)
	if angle_val > 2*math.pi:
		angle_val = angle_val % (2*math.pi)

	return linear_acc,angular_acc,linear_speed,radius,angular_speed,angle_val

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
	orb_r = r/(10**9)
	for i in range(num_cal_frame):
		lin_acc,ang_acc,lin_v,r,ang_v,angle = full_update(lin_acc,ang_acc,r,lin_v,ang_v,angle,del_t)
		earth_x,earth_y = update_pos(earth_x,earth_y,angle,orb_r) 
		pg.draw.circle(window,pg.Color("blue"),(int(round(earth_x,0)),int(round(earth_y,0))),earth_r,0)
		orb_list.append([earth_x,earth_y]) 

	planet_v = math.sqrt(const_G*mass_sun/(r)) * 10**(-3)
	print(lin_v,planet_v)
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
