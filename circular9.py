import pygame as pg
from pygame.locals import *
import math

pg.init()
window = pg.display.set_mode((800,800)) # size of the screen
pg.display.set_caption("The Solar System")

sun_x = 400
sun_y = 400
sun_r = 50
mass_sun = 2*10**(30)
const_G = 6.67*10**(-11)

# control variables
tcont_orb_r = 150*10**9
cont_orb_r = tcont_orb_r/(10**9)
cont_lin_v = 0 #m/s
cont_angle = math.pi/2 # rad
cont_x = 400
cont_y = 250
cont_r = 15

num_cal_frame = 10
del_t = 3600*24/num_cal_frame
collide_but = False

# variables for planets

# Mercury
mercury_x = 400
mercury_y = 300
mercury_r = 8
mercury_orb_r = 100 # 150*10^6 km
mercury_period = 88

# Venus
venus_x = 400
venus_y = 225
venus_r = 15
venus_orb_r = 125 # 150*10^6 km
venus_period = 225

# Earth
earth_x = 400
earth_y = 250
earth_r = 15
earth_orb_r = 150 # 150*10^6 km
earth_period = 365

# Mars
mars_x = 400
mars_y = 250
mars_r = 8
mars_orb_r = 175 # 150*10^6 km
mars_period = 687

# Jupiter
jupiter_x = 400
jupiter_y = 250
jupiter_r = 70
jupiter_orb_r = 225 # 150*10^6 km
jupiter_period = 4331

# Saturn
saturn_x = 400
saturn_y = 250
saturn_r = 60
saturn_orb_r = 250 # 150*10^6 km
saturn_period = 10474

# Uranus
uranus_x = 400
uranus_y = 250
uranus_r = 25
uranus_orb_r = 300 # 150*10^6 km
uranus_period = 30589

# Neptune
neptune_x = 400
neptune_y = 250
neptune_r = 24
neptune_orb_r = 325 # 150*10^6 km
neptune_period = 59800

count = 1

# orbital list
orb_list = []

# text
pg.font.init()
def DrawText(text,x,y,textHeight=30,fontColor=(255,255,255),backgroudColor=(0,0,0),fontType="Graduate.ttf"):
	# Set the font of the text
	font = pg.font.Font(fontType, textHeight)
	textCont = font.render(text, True,fontColor,backgroudColor)
	textPos = textCont.get_rect() 
	textPos.center = (x,y)

	return textCont,textPos


first_flag = True
def firstScreen():
	# Set up background
	background = pg.image.load('bg3.jpeg').convert()
	# Set up button
	startButton = pg.image.load('sb.png')
	flashLight = pg.image.load('fl.png')

	# Display the moving flashLight
	x, y = pg.mouse.get_pos()
	x-= flashLight.get_width() / 2
	y-= flashLight.get_height() / 2

	# Display background
	window.blit(background,(0,0))

	# Display button
	window.blit(startButton,(300,600))

	# Draw Title
	title1_cont,title1_pos = DrawText("Space",400,180,textHeight = 90,fontType = "font.ttf")
	window.blit(title1_cont,title1_pos) 
	title2_cont,title2_pos = DrawText("HUB",400,270,textHeight = 76,fontType = "font.ttf")
	window.blit(title2_cont,title2_pos)

	# Display flash flight
	window.blit(flashLight, (x, y))

# tool bar font
tb_font = pg.font.Font("digit.ttf",12)

# Control bar
#creating text
def txt_setup(size,text,color):
	#create font with parameters of func
	f=pg.font.Font("digit.ttf",size)
	#render a text image from previous font.
	#The parameter True turns on anti aliasing (smoother letters)
	t=f.render(text,True,pg.Color(color))
	return(t)

#txt box and txt vars
cont_but = False
userV = math.sqrt(const_G*mass_sun/(earth_orb_r*10**9)) * 10**(-3)
text_box=[330,360,150,100]
text2_box = [300,420,250,50]
box_color="gray"
typing=False
text=str(int(userV))
#initial text size
t=txt_setup(40,text,"White")


# planet fact

class fact_planet:
	def __init__(self,pic,name,mass,diameter,escape_v,rat_period,orb_radius,orb_period,orb_velocity,mean_temp,num_moon,info2,info3):
		self.pic = pic
		self.name = name
		self.mass = mass
		self.diameter = diameter
		self.escape_v = escape_v
		self.rat_period = rat_period
		self.orb_radius = orb_radius
		self.orb_period = orb_period
		self.orb_velocity = orb_velocity
		self.mean_temp = mean_temp
		self.num_moon = num_moon
		self.info2 = info2
		self.info3 = info3

	def set_text(self,text,textHeight=16,fontType="SpecialElite.ttf"): # alternative options: "Graduate.ttf"
		font = pg.font.Font(fontType,textHeight)
		text = font.render(text,True,(255,255,255))
		return text

	def display(self):
		self.out_text_name = self.set_text(self.name,textHeight=30,fontType="SpecialElite.ttf")
		window.blit(self.out_text_name,(200,590))
		
		self.in_text_mass = "Mass:  " + str(self.mass) + " *10^24 kg"
		self.out_text_mass = self.set_text(str(self.in_text_mass))
		window.blit(self.out_text_mass,(210,620))

		self.in_text_diameter = "Diameter:  " + str(self.diameter) + " *10^6 km"
		self.out_text_diameter = self.set_text(str(self.in_text_diameter))
		window.blit(self.out_text_diameter,(210,640))

		self.in_text_ev = "Escape Velocity:  " + str(self.escape_v) + " km/s"
		self.out_text_ev = self.set_text(str(self.in_text_ev))
		window.blit(self.out_text_ev,(210,660))

		self.in_text_rp = "Rotational Period:  " + str(self.rat_period) + " hours"
		self.out_text_rp = self.set_text(str(self.in_text_rp))
		window.blit(self.out_text_rp,(210,680))

		self.in_text_or = "Orbital Radius:  " + str(self.orb_radius) + " km"
		self.out_text_or = self.set_text(str(self.in_text_or))
		window.blit(self.out_text_or,(210,700))

		self.in_text_op = "Orbital Period:  " + str(self.orb_period) + " days"
		self.out_text_op = self.set_text(str(self.in_text_op))
		window.blit(self.out_text_op,(210,720))

		self.in_text_ov = "Orbital Velocity:  " + str(self.orb_velocity) + " km/s"
		self.out_text_ov = self.set_text(str(self.in_text_ov))
		window.blit(self.out_text_ov,(480,600))

		self.in_text_mt = "Mean Temperature:  " + str(self.mean_temp) + " celcius"
		self.out_text_mt = self.set_text(str(self.in_text_mt))
		window.blit(self.out_text_mt,(480,620))	

		self.in_text_nm = "Number of moons:  " + str(self.num_moon)
		self.out_text_nm = self.set_text(str(self.in_text_nm))
		window.blit(self.out_text_nm,(480,640))			

		self.in_text_info1 = "Interesting Fact"
		self.out_text_info1 = self.set_text(str(self.in_text_info1),textHeight=30)
		window.blit(self.out_text_info1,(480,660))	

		self.out_text_info2 = self.set_text(self.info2,fontType="SpecialElite.ttf")
		window.blit(self.out_text_info2,(500,700))

		self.out_text_info3 = self.set_text(self.info3,fontType="SpecialElite.ttf")
		window.blit(self.out_text_info3,(500,720))	

		window.blit(self.pic[0],(90,650))

# background
background = pg.image.load("bg1.jpg")

# tool bar design
toolBar = pg.image.load('marbleBar1.png')
tb_mercury = pg.image.load('mercury.png')
tb_venus = pg.image.load('venus.png')
tb_earth = pg.image.load('earth_black.png')
tb_mars = pg.image.load('mars_curiosity.png')
tb_jupiter = pg.image.load('jupiter.png')
tb_saturn = pg.image.load('saturn.png')
tb_uranus = pg.image.load('uranus.png')
tb_nepture = pg.image.load('nepture.png')
tb_toggles = pg.image.load('toggles.png')
tb_play = pg.image.load('play.png')
tb_reset = pg.image.load('reset.png')
tb_info = pg.image.load('info.png')
tb_exit = pg.image.load('exit.png')

# control bar design
cont_text_bar = pg.image.load('control.png')
collide_text = pg.image.load('collide.png')
reset_but = False

class tb_text: # need reference
	hover_flag = False
	def __init__(self,text,pos):
		self.text = text
		self.pos = pos
		self.set_rect()
		self.display()

	def display(self):
		self.set_range()
		window.blit(self.range,self.rect)

	def set_range(self):
		self.range = tb_font.render(self.text,True,self.color())

	def color(self):
		if self.hover_flag:
			return (0,0,0)
		else:
			return (100,100,100)

	def set_rect(self):
		self.set_range()
		self.rect = self.range.get_rect()
		self.rect.topleft = self.pos

hover_tb = [tb_text("Mercury",(25,75)),tb_text("Venus",(90,75)),tb_text("Earth",(150,75)),tb_text("Mars",(210,75)),tb_text("Jupiter",(265,75)),tb_text("Saturn",(325,75)),tb_text("Uranus",(385,75)),tb_text("Nepture",(445,75)),tb_text("Control",(506,75)),tb_text("Play",(575,75)),tb_text("Reset",(630,75)),tb_text("Info",(690,75)),tb_text("Exit",(745,75))]


class showBar:
	def __init__(self,show_bar,planet,gif):
		self.show_bar = show_bar
		self.planet = planet
		self.gif = gif

	def display(self):
		window.blit(self.show_bar,(0,570))
		self.sf1_cont,self.sf1_pos = DrawText("Planet", 100,585,textHeight=35,fontType="font.ttf")
		self.sf2_cont,self.sf2_pos = DrawText("Fact", 140,625,textHeight=35,fontType="font.ttf")
		window.blit(self.sf1_cont,self.sf1_pos)
		window.blit(self.sf2_cont,self.sf2_pos)
		self.show_planet_fact()

	def show_planet_fact(self):
		# show bar - planet fact
		if self.planet == "Mercury":
			fp_planet = fact_planet(self.gif,self.planet,0.330,4879,4.3,1407.6,57.9,88,47.4,167,0,"Mercury is hot!!","But not too hot for ice??")
			fp_planet.display()

		elif self.planet == "Venus":
			fp_planet = fact_planet(self.gif,self.planet,4.87,12104,10.4,-5832.5,108.9,224.7,35.0,464,0,"Venus has no moons...","we are not sure why.")
			fp_planet.display()
		
		elif self.planet == "Earth":
			fp_planet = fact_planet(self.gif,self.planet,5.97,12756,11.2,23.9,152.1,365.2,29.8,15,1,"The Rotation of the Earth is","gradually slowing down!!")
			fp_planet.display()

		elif self.planet == "Mars":
			fp_planet = fact_planet(self.gif,self.planet,0.642,6792,5.0,24.6,249.2,687.0,24.1,-65,2,"Nicked name: Red planet","with a pickish atomosphere!!")
			fp_planet.display()

		elif self.planet == "Jupiter":
			fp_planet = fact_planet(self.gif,self.planet,1898,142984,59.5,9.9,816.6,4331,13.1,-110,79,"Jupiter is a great","COMET CATCHER!!")
			fp_planet.display()

		elif self.planet == "Saturn":
			fp_planet = fact_planet(self.gif,self.planet,568,120536,35.5,10.7,1514.5,10747,9.7,-140,82,"No one knows...","how old Saturn's rings are!!")
			fp_planet.display()

		elif self.planet == "Uranus":
			fp_planet = fact_planet(self.gif,self.planet,86.8,51118,21.3,-17.2,3003.6,30589,6.8,-195,27,"Uranus is dubbed as an...","ICED GIANT~")
			fp_planet.display()

		elif self.planet == "Nepture":
			fp_planet = fact_planet(self.gif,self.planet,102,49528,23.5,16.1,4545.7,59800,5.4,-200,14,"The descovery of Nepture is","still a controversy...")
			fp_planet.display()
		

# toggle bar
toggle_bar = pg.image.load('show_bar2.png')
# show bar
show_bar = pg.image.load('show_bar.png')

# sun and planet gif
# sun
sun_index = 0
sun_gif00 = pg.image.load('./sun2/05.gif')
sun_gif01 = pg.image.load('./sun2/06.gif')
sun_gif02 = pg.image.load('./sun2/13.gif')
sun_gif03 = pg.image.load('./sun2/14.gif')
sun_gif04 = pg.image.load('./sun2/15.gif')
sun_gif05 = pg.image.load('./sun2/16.gif')
sun_gif06 = pg.image.load('./sun2/17.gif')
sun_gif07 = pg.image.load('./sun2/18.gif')

sun_gif = [sun_gif00,sun_gif01,sun_gif02,sun_gif03,sun_gif04,sun_gif05,sun_gif06,sun_gif07]

# mercury
flag_mercury = False
mercury_index = 0
mercury_gif00 = pg.image.load('./mercury/00.gif')
mercury_gif01 = pg.image.load('./mercury/05.gif')
mercury_gif02 = pg.image.load('./mercury/10.gif')
mercury_gif03 = pg.image.load('./mercury/15.gif')
mercury_gif04 = pg.image.load('./mercury/20.gif')

mercury_gif = [mercury_gif00,mercury_gif01,mercury_gif02,mercury_gif03,mercury_gif04]

# venus
flag_venus = False
venus_index = 0
venus_gif00 = pg.image.load('./venus/00.gif')
venus_gif01 = pg.image.load('./venus/04.gif')
venus_gif02 = pg.image.load('./venus/08.gif')
venus_gif03 = pg.image.load('./venus/12.gif')
venus_gif04 = pg.image.load('./venus/16.gif')

venus_gif = [venus_gif00,venus_gif01,venus_gif02,venus_gif03,venus_gif04]

# earth
flag_earth = False
earth_index = 0
earth_gif00 = pg.image.load('./earth2/00.gif')
earth_gif01 = pg.image.load('./earth2/01.gif')
earth_gif02 = pg.image.load('./earth2/02.gif')
earth_gif03 = pg.image.load('./earth2/03.gif')
earth_gif04 = pg.image.load('./earth2/04.gif')

earth_gif = [earth_gif00,earth_gif01,earth_gif02,earth_gif03,earth_gif04]

# mars
mars_index = 0
mars_gif00 = pg.image.load('./mars/00.gif')
mars_gif01 = pg.image.load('./mars/04.gif')
mars_gif02 = pg.image.load('./mars/08.gif')
mars_gif03 = pg.image.load('./mars/12.gif')
mars_gif04 = pg.image.load('./mars/16.gif')

mars_gif = [mars_gif00,mars_gif01,mars_gif02,mars_gif03,mars_gif04]

# jupiter
jupiter_index = 0
jupiter_gif00 = pg.image.load('./jupiter/00.gif')
jupiter_gif01 = pg.image.load('./jupiter/05.gif')
jupiter_gif02 = pg.image.load('./jupiter/10.gif')
jupiter_gif03 = pg.image.load('./jupiter/15.gif')
jupiter_gif04 = pg.image.load('./jupiter/20.gif')

jupiter_gif = [jupiter_gif00,jupiter_gif01,jupiter_gif02,jupiter_gif03,jupiter_gif04]

# saturn
saturn_index = 0
saturn_gif00 = pg.image.load('./saturn/00.gif')
saturn_gif01 = pg.image.load('./saturn/05.gif')
saturn_gif02 = pg.image.load('./saturn/10.gif')
saturn_gif03 = pg.image.load('./saturn/15.gif')
saturn_gif04 = pg.image.load('./saturn/20.gif')

saturn_gif = [saturn_gif00,saturn_gif01,saturn_gif02,saturn_gif03,saturn_gif04]

# uranus
uranus_index = 0
uranus_gif00 = pg.image.load('./uranus/00.gif')
uranus_gif01 = pg.image.load('./uranus/10.gif')
uranus_gif02 = pg.image.load('./uranus/20.gif')
uranus_gif03 = pg.image.load('./uranus/30.gif')
uranus_gif04 = pg.image.load('./uranus/40.gif')

uranus_gif = [uranus_gif00,uranus_gif01,uranus_gif02,uranus_gif03,uranus_gif04]

# neptune
neptune_index = 0
neptune_gif00 = pg.image.load('./neptune/00.gif')
neptune_gif01 = pg.image.load('./neptune/04.gif')
neptune_gif02 = pg.image.load('./neptune/08.gif')
neptune_gif03 = pg.image.load('./neptune/12.gif')
neptune_gif04 = pg.image.load('./neptune/16.gif')

neptune_gif = [neptune_gif00,neptune_gif01,neptune_gif02,neptune_gif03,neptune_gif04]

# show planet
show_planet = showBar(show_bar,"Earth",earth_gif)

# flag
info = "Earth"
planet_index = 0

# draw the earth
def flag(info):
	flag_planet = info
	if flag_planet == "Earth":
		planet_orb_r = earth_orb_r
		planet_period = earth_period
		planet_gif = earth_gif
		planet_r = earth_r
		planet_x = earth_x
		planet_y = earth_y
	elif flag_planet == "Mercury":
		planet_orb_r = mercury_orb_r
		planet_period = mercury_period
		planet_gif = mercury_gif
		planet_r = mercury_r
		planet_x = mercury_x
		planet_y = mercury_y
	elif flag_planet == "Venus":
		planet_orb_r = venus_orb_r
		planet_period = venus_period
		planet_gif = venus_gif
		planet_r = venus_r
		planet_x = venus_x
		planet_y = venus_y
	elif flag_planet == "Mars":
		planet_orb_r = mars_orb_r
		planet_period = mars_period
		planet_gif = mars_gif
		planet_r = mars_r
		planet_x = mars_x
		planet_y = mars_y
	elif flag_planet == "Jupiter":
		planet_orb_r = jupiter_orb_r
		planet_period = jupiter_period
		planet_gif = jupiter_gif
		planet_r = jupiter_r
		planet_x = jupiter_x
		planet_y = jupiter_y
	elif flag_planet == "Saturn":
		planet_orb_r = saturn_orb_r
		planet_period = saturn_period
		planet_gif = saturn_gif
		planet_r = saturn_r
		planet_x = saturn_x
		planet_y = saturn_y
	elif flag_planet == "Uranus":
		planet_orb_r = uranus_orb_r
		planet_period = uranus_period
		planet_gif = uranus_gif
		planet_r = uranus_r
		planet_x = uranus_x
		planet_y = uranus_y
	else:
		planet_orb_r = neptune_orb_r
		planet_period = neptune_period
		planet_gif = neptune_gif
		planet_r = neptune_r
		planet_x = neptune_x
		planet_y = neptune_y
	return planet_orb_r,planet_period,planet_gif,planet_r,planet_x,planet_y

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

# implement rectangle collision first then improve it using the circular collision
def rect_collide(x1,y1,r1,x2,y2,r2):
	l_x = x1-r1
	t_y = y1-r1
	r_x = x1+r1
	b_y = y1+r1

	flag = False

	if (((x2-r2) <= r_x) and ((x2-r2) >= l_x)) or (((x2+r2) <= r_x) and (x2+r2) >= l_x):
		if (((y2-r2) <= b_y) and ((y2-r2) >= t_y)) or (((y2+r2) <= b_y) and (y2+r2) >= t_y):
			flag = True
	return flag 

def rotate_planet(planet_x,planet_y,planet_orb_r,planet_period):
	cur_period = planet_period
	if cur_period > 1000:
		cur_period /= 10
	elif cur_period > 10000:
		cur_period /= 10000
	planet_x, planet_y = cur_pos(sun_x,sun_y-planet_orb_r,cur_period,planet_orb_r) 
	orb_list.append([planet_x,planet_y])

	# draw the orbital
	for i in range(0,len(orb_list)):
		pg.draw.rect(window,pg.Color("White"),(orb_list[i][0],orb_list[i][1],8,8),0)

	if len(orb_list) == 100: # the length of the trail
		orb_list.pop(0)

	return planet_x,planet_y,planet_orb_r,planet_period

# control planet function
cont_but = False
start_but = False

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

def update_pos(x,y,angle_val,orb_r):
	x = math.cos(angle_val) * orb_r + 400
	y = math.sin(-angle_val) * orb_r + 400
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

def control_planet(planet_x,planet_y,planet_orb_r,planet_period,linear_acc,angular_acc,linear_speed,angular_speed,angle_val,deltaT,num_cal_frame):	
	for i in range(num_cal_frame):
		linear_acc,angular_acc,linear_speed,planet_orb_r,angular_speed,angle_val = full_update(linear_acc,angular_acc,planet_orb_r,linear_speed,angular_speed,angle_val,deltaT)
		orb_r = planet_orb_r/(10**9)
		planet_x,planet_y = update_pos(planet_x,planet_y,angle_val,orb_r) 
	orb_list.append([planet_x,planet_y])
	
	# draw the orbital
	for i in range(0,len(orb_list)):
		pg.draw.rect(window,pg.Color("White"),(orb_list[i][0],orb_list[i][1],8,8),0)

	return planet_x,planet_y,linear_acc,angular_acc,linear_speed,planet_orb_r,angular_speed,angle_val

run = True
while run:
	# delay for showing the slow motion 
	pg.time.delay(1)

	print("cont_but:",cont_but,"reset_but:",reset_but,"start_but:",start_but)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		elif pg.mouse.get_pressed()[0]:
			if (pg.mouse.get_pos()[0] >= 730) and (pg.mouse.get_pos()[0] <= 800):
				if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
					first_flag = True
			if (pg.mouse.get_pos()[0] >= 280) and (pg.mouse.get_pos()[0] <= 600):
				if (pg.mouse.get_pos()[1] >= 600) and (pg.mouse.get_pos()[1] <= 800):
					first_flag = False
			if (pg.mouse.get_pos()[0] >= 500) and (pg.mouse.get_pos()[0] <= 560):
				if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
					cont_but = True
			if (pg.mouse.get_pos()[0] >= 560) and (pg.mouse.get_pos()[0] <= 620):
				if (pg.mouse.get_pos()[1] > 12) and (pg.mouse.get_pos()[1] <= 80):
					start_but = True
					orb_list = []
			if (pg.mouse.get_pos()[0] >= 620) and (pg.mouse.get_pos()[0] <= 675):
				if (pg.mouse.get_pos()[1] > 12) and (pg.mouse.get_pos()[1] <= 80):
					reset_but = True
					orb_list = []


		# detecting key presses
		if (event.type==pg.MOUSEBUTTONDOWN) and (cont_but == True):
			if typing==False:
				box_color="black"
				typing=True
		if event.type==pg.KEYDOWN and (cont_but == True):
			if event.key==pg.K_RETURN and typing==True:
				box_color="gray"
				typing=False
			elif event.key==pg.K_BACKSPACE:
				#remove last string letter
				text=text[:-1]
				#update text image surface
				t = txt_setup(40,str(text),"White")
			else:
				#from unicode get letter of text
				#you can use try and except to detect if event.unicode is a number here
				text += event.unicode
				userV = int(text)
				#update text image surface
				t = txt_setup(40,str(text),"White")


	window.fill((0,0,0))
	# background
	window.blit(background,(0,0))

	# if reset_but == False:
	if first_flag:
		firstScreen()
	else:
		# draw the sun
		if sun_index == 8:
			sun_index = 0
		sun_curgif = sun_gif[sun_index]
		window.blit(sun_curgif,(350,350))
		sun_index += 1

		# control
		if cont_but:
			cont_v = userV * 10**3
			tcont_orb_r = const_G*mass_sun/(cont_v**2)
			cont_orb_r = cont_orb_r / (10**9)
			# draw text box
			pg.draw.rect(window,pg.Color(box_color),(text2_box[0],text2_box[1],text2_box[2],text2_box[3]),1)
			# draw text
			window.blit(t,(int(text2_box[0]+text2_box[2]/2-t.get_width()/2),int(text2_box[1]+text2_box[3]/2-t.get_height()/2)))
			# draw text background
			window.blit(cont_text_bar,(int(text_box[0]+text_box[2]/2-t.get_width()/2)-180,int(text_box[1]+text_box[3]/2-t.get_height()/2)-100))

		if reset_but:
			userV = math.sqrt(const_G*mass_sun/(earth_orb_r*10**9)) * 10**(-3)
			tcont_orb_r = 150*10**9
			cont_orb_r = tcont_orb_r/(10**9)
			cont_lin_v = 0 #m/s
			cont_angle = math.pi/2 # rad
			cont_x = 400
			cont_y = 250
			cont_r = 15
			reset_but = False
			collide_but = False
			start_but = False

		if collide_but:
			window.blit(collide_text,(int(text_box[0]+text_box[2]/2-t.get_width()/2)-180,int(text_box[1]+text_box[3]/2-t.get_height()/2)-100))

		if start_but:
			cont_but = False
			cont_ang_v = 2*10**(-7)
			cont_lin_acc = tcont_orb_r*(cont_ang_v**2)-((const_G*mass_sun)/(tcont_orb_r**2)) #m/s^2
			cont_ang_acc = -(2*cont_lin_v*cont_ang_v)/tcont_orb_r #rad/s^2
			cont_x,cont_y,cont_lin_acc,cont_ang_acc,cont_lin_v,tcont_orb_r,cont_ang_v,cont_angle = control_planet(cont_x,cont_y,tcont_orb_r,365,cont_lin_acc,cont_ang_acc,cont_lin_v,cont_ang_v,cont_angle,del_t,num_cal_frame)

			if earth_index == 5:
				earth_index = 0
			cont_curgif = earth_gif[earth_index]
			window.blit(cont_curgif,(int(cont_x)-cont_r,int(cont_y)-cont_r))
			earth_index += 1

			# Calculate velocity
			if collide_but == False:
				planet_v = math.sqrt(const_G*mass_sun/(tcont_orb_r)) * 10**(-3)

			text_v,pos_v = DrawText("VELOCITY", 140,120,textHeight=30,fontType="font.ttf")
			content_v = str(int(planet_v)) + " km/s"
			tv_v,pos_tv_v = DrawText(content_v,160,160,textHeight=20)
			content_r = str(int(tcont_orb_r/(10**9))) + " km"
			text_r,pos_r = DrawText("RADIUS", 400,120,textHeight=30,fontType="font.ttf")
			tv_r,pos_tv_r = DrawText(content_r,420,160,textHeight=20)
			content_p = "N/A days"
			text_p,pos_p = DrawText("PERIOD", 660,120,textHeight=30,fontType="font.ttf")
			tv_p,pos_tv_p = DrawText(content_p,680,160,textHeight=20) 

			# if it collides with the sun
			if rect_collide(400,400,sun_r,cont_x,cont_y,cont_r):
				start_but = False
				collide_but = True


		elif (start_but == False) and (collide_but == False):
			planet_orb_r,planet_period,planet_gif,planet_r,planet_x,planet_y = flag(info)
			planet_x,planet_y,planet_orb_r,planet_period = rotate_planet(planet_x,planet_y,planet_orb_r,planet_period)
			# increment the count value
			count += 1
			if planet_index == 5:
				planet_index = 0
			planet_curgif = planet_gif[planet_index]
			window.blit(planet_curgif,(planet_x-planet_r,planet_y-planet_r))
			planet_index += 1

			show_planet.display()
			if pg.mouse.get_pressed()[0]:
				if (pg.mouse.get_pos()[0] >= 20) and (pg.mouse.get_pos()[0] <= 80):
					if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
						show_planet = showBar(show_bar,"Mercury",mercury_gif)
						info = "Mercury"
				if (pg.mouse.get_pos()[0] >= 80) and (pg.mouse.get_pos()[0] <= 140):
					if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
						show_planet = showBar(show_bar,"Venus",venus_gif)
						info = "Venus"
				if (pg.mouse.get_pos()[0] >= 140) and (pg.mouse.get_pos()[0] <= 200):
					if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
						show_planet = showBar(show_bar,"Earth",earth_gif)
						info = "Earth"
				if (pg.mouse.get_pos()[0] >= 200) and (pg.mouse.get_pos()[0] <= 260):
					if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
						show_planet = showBar(show_bar,"Mars",mars_gif)
						info = "Mars"
				if (pg.mouse.get_pos()[0] >= 260) and (pg.mouse.get_pos()[0] <= 320):
					if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
						show_planet = showBar(show_bar,"Jupiter",jupiter_gif)
						info = "Jupiter"
				if (pg.mouse.get_pos()[0] >= 320) and (pg.mouse.get_pos()[0] <= 380):
					if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
						show_planet = showBar(show_bar,"Saturn",saturn_gif)
						info = "Saturn"
				if (pg.mouse.get_pos()[0] >= 380) and (pg.mouse.get_pos()[0] <= 440):
					if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
						show_planet = showBar(show_bar,"Uranus",uranus_gif)
						info = "Uranus"
				if (pg.mouse.get_pos()[0] >= 440) and (pg.mouse.get_pos()[0] <= 490):
					if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
						show_planet = showBar(show_bar,"Nepture",neptune_gif)
						info = "Nepture"
			

			# Calculate velocity
			planet_v = math.sqrt(const_G*mass_sun/(planet_orb_r*10**9)) * 10**(-3)

			text_v,pos_v = DrawText("VELOCITY", 140,120,textHeight=30,fontType="font.ttf")
			content_v = str(int(planet_v)) + " km/s"
			tv_v,pos_tv_v = DrawText(content_v,160,160,textHeight=20)
			content_r = str(int(planet_orb_r)) + " km"
			text_r,pos_r = DrawText("RADIUS", 400,120,textHeight=30,fontType="font.ttf")
			tv_r,pos_tv_r = DrawText(content_r,420,160,textHeight=20)
			content_p = str(int(planet_period)) + " days"
			text_p,pos_p = DrawText("PERIOD", 660,120,textHeight=30,fontType="font.ttf")
			tv_p,pos_tv_p = DrawText(content_p,680,160,textHeight=20) 


		# draw the text
		window.blit(text_v,pos_v)
		window.blit(tv_v,pos_tv_v)
		window.blit(text_r,pos_r)
		window.blit(tv_r,pos_tv_r)
		window.blit(text_p,pos_p)
		window.blit(tv_p,pos_tv_p)


		# tool bar
		window.blit(toolBar,(0,10))
		window.blit(tb_mercury,(20,12))
		window.blit(tb_venus,(80,12))
		window.blit(tb_earth,(140,12))
		window.blit(tb_mars,(200,12))
		window.blit(tb_jupiter,(260,12))
		window.blit(tb_saturn,(320,12))
		window.blit(tb_uranus,(380,12))
		window.blit(tb_nepture,(440,12))
		window.blit(tb_toggles,(500,12))
		window.blit(tb_play,(560,12))
		window.blit(tb_reset,(620,12))
		window.blit(tb_info,(675,12))
		window.blit(tb_exit,(730,12))

		for i in hover_tb:
			if i.rect.collidepoint(pg.mouse.get_pos()):
				i.hover_flag = True
			else:
				i.hover_flag = False
			i.display()

		# show bar
		window.blit(toggle_bar,(0,90))

	# update the screen
	pg.display.update()

pg.quit()
