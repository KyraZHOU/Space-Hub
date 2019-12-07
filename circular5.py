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

# time interval
del_t = 0.05


# slider
slider_x = 30
# value_x = math.sqrt(const_G*mass_sun/(earth_orb_r*10**9)) * 10**(-3)
true_v = math.sqrt(const_G*mass_sun/(earth_orb_r*10**9)) * 10**(-3)
value_x = true_v
max_v = (math.sqrt(const_G*mass_sun/(earth_orb_r*10**9)) * 2)*10**(-3) # 59479.1392 m/s = 60 km/s
# min_v = (math.sqrt(const_G*mass_sun/(earth_orb_r*10**9)) * 1/2)*10**(-3) # 14869.7848 m/s = 15 km/s
min_v = 1

slider2_x = 290
max_radius = ((const_G*mass_sun)/(max_v*10**(3))**2)*10**(-9) # convert into km
min_radius = ((const_G*mass_sun)/(min_v*10**(3))**2)*10**(-9) # convert into km

slider3_x = 550
slider_length = 200


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

text_v,pos_v = DrawText("VELOCITY", 140,120,textHeight=30,fontType="font.ttf")
cont_v = str(int(value_x)) + " km/s"
tv_v,pos_tv_v = DrawText(cont_v,160,160,textHeight=20)
cont_r = str(int(earth_orb_r)) + " km"
text_r,pos_r = DrawText("RADIUS", 400,120,textHeight=30,fontType="font.ttf")
tv_r,pos_tv_r = DrawText(cont_r,420,160,textHeight=20)
cont_p = str(int(earth_period)) + " days"
text_p,pos_p = DrawText("PERIOD", 660,120,textHeight=30,fontType="font.ttf")
tv_p,pos_tv_p = DrawText(cont_p,680,160,textHeight=20)

# tool bar font
tb_font = pg.font.Font("digit.ttf",12)

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


# boolean variables
pause = False

# button var
button_range = [500,500,100,20] 
button_color=(160,0,100)

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
tb_pause = pg.image.load('pause.png')
tb_info = pg.image.load('info.png')
tb_exit = pg.image.load('exit.png')

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

hover_tb = [tb_text("Mercury",(25,75)),tb_text("Venus",(90,75)),tb_text("Earth",(150,75)),tb_text("Mars",(210,75)),tb_text("Jupiter",(265,75)),tb_text("Saturn",(325,75)),tb_text("Uranus",(385,75)),tb_text("Nepture",(445,75)),tb_text("Control",(506,75)),tb_text("Play",(575,75)),tb_text("Pause",(630,75)),tb_text("Info",(690,75)),tb_text("Exit",(745,75))]


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
			fp_planet = fact_planet(self.gif,self.planet,86.8,51118,21.3,-17.2,3003.6,30589,6.8,-195,27,"The Rotation of the Earth is","gradually slowing down!!")
			fp_planet.display()

		elif self.planet == "Nepture":
			fp_planet = fact_planet(self.gif,self.planet,102,49528,23.5,16.1,4545.7,59800,5.4,-200,14,"The Rotation of the Earth is","gradually slowing down!!")
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

mercury_gif = [mercury_gif00]

# venus
flag_venus = False
venus_index = 0
venus_gif00 = pg.image.load('./venus/00.gif')

venus_gif = [venus_gif00]

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

mars_gif = [mars_gif00]

# jupiter
jupiter_index = 0
jupiter_gif00 = pg.image.load('./jupiter/00.gif')

jupiter_gif = [jupiter_gif00]

# saturn
saturn_index = 0
saturn_gif00 = pg.image.load('./saturn/00.gif')

saturn_gif = [saturn_gif00]

# uranus
uranus_index = 0
uranus_gif00 = pg.image.load('./uranus/00.gif')

uranus_gif = [uranus_gif00]

# neptune
neptune_index = 0
neptune_gif00 = pg.image.load('./neptune/00.gif')

neptune_gif = [neptune_gif00]

# show planet
show_planet = showBar(show_bar,"Earth",earth_gif)


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

run = True
while run:
	# delay for showing the slow motion 
	pg.time.delay(1)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		'''
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
		if event.type == pg.MOUSEBUTTONDOWN:
			if pg.mouse.get_pos()[0] >= button_range[0] and pg.mouse.get_pos()[0] <= (button_range[0] + button_range[2]): #x-y
				if pg.mouse.get_pos()[1] >= button_range[1] and pg.mouse.get_pos()[1] <= (button_range[1] + button_range[3]):
					button_color = (200,40,140) # darker button
		if event.type == pg.MOUSEBUTTONUP:
			if pg.mouse.get_pos()[0] >= button_range[0] and pg.mouse.get_pos()[0] <= (button_range[0] + button_range[2]): #x-y
				if pg.mouse.get_pos()[1] >= button_range[1] and pg.mouse.get_pos()[1] <= (button_range[1] + button_range[3]):
					button_color = (160,0,100) # colour back
					# add function
		'''

	window.fill((0,0,0))
	# background
	window.blit(background,(0,0))
	# draw the sun
	if sun_index == 8:
		sun_index = 0
	sun_curgif = sun_gif[sun_index]
	window.blit(sun_curgif,(350,350))
	sun_index += 1
	# pg.draw.circle(window,pg.Color("red"),(sun_x,sun_y),sun_r,0)

	
	# draw the text
	# pg.draw.rect(window,pg.Color("white"),(15,15,240,60),0)
	# text_v = font.render("Orbital Veclocity: "+str(round(value_x,2)) + " km/s",True,(0,0,0)) # antialias - smooth curves
	window.blit(text_v,pos_v)
	window.blit(tv_v,pos_tv_v)
	# pg.draw.rect(window,pg.Color("white"),(275,15,240,60),0)
	# text_r = font.render("Orbital radius: " + str(round(earth_orb_r,1)) + " km",True,(0,0,0))
	window.blit(text_r,pos_r)
	window.blit(tv_r,pos_tv_r)
	# pg.draw.rect(window,pg.Color("white"),(535,15,240,60),0)
	# text_p = font.render("Orbital period: " + str(round(earth_period,0)) + " days",True,(0,0,0))
	window.blit(text_p,pos_p)
	window.blit(tv_p,pos_tv_p)

	'''
	# draw the scale
	pg.draw.rect(window,pg.Color("gray"),(30,55,slider_length,10),0)
	pg.draw.circle(window,pg.Color("black"),(slider_x,60),10,0)

	pg.draw.rect(window,pg.Color("gray"),(290,55,slider_length,10),0)
	pg.draw.circle(window,pg.Color("black"),(int(slider2_x),60),10,0)

	pg.draw.rect(window,pg.Color("gray"),(550,55,slider_length,10),0)
	pg.draw.circle(window,pg.Color("black"),(slider3_x,60),10,0)
	'''
	show_planet.display()
	if pg.mouse.get_pressed()[0]:
		if (pg.mouse.get_pos()[0] >= 20) and (pg.mouse.get_pos()[0] <= 80):
			if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
				# flag_mercury = not flag_mercury 
				show_planet = showBar(show_bar,"Mercury",mercury_gif)
		if (pg.mouse.get_pos()[0] >= 80) and (pg.mouse.get_pos()[0] <= 140):
			if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
				# flag_venus = not flag_venus
				show_planet = showBar(show_bar,"Venus",venus_gif)
		if (pg.mouse.get_pos()[0] >= 140) and (pg.mouse.get_pos()[0] <= 200):
			if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
				# flag_earth = not flag_earth
				show_planet = showBar(show_bar,"Earth",earth_gif)
		if (pg.mouse.get_pos()[0] >= 200) and (pg.mouse.get_pos()[0] <= 260):
			if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
				show_planet = showBar(show_bar,"Mars",mars_gif)
		if (pg.mouse.get_pos()[0] >= 260) and (pg.mouse.get_pos()[0] <= 320):
			if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
				show_planet = showBar(show_bar,"Jupiter",jupiter_gif)
		if (pg.mouse.get_pos()[0] >= 320) and (pg.mouse.get_pos()[0] <= 380):
			if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
				show_planet = showBar(show_bar,"Saturn",saturn_gif)
		if (pg.mouse.get_pos()[0] >= 380) and (pg.mouse.get_pos()[0] <= 440):
			if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
				show_planet = showBar(show_bar,"Uranus",uranus_gif)
		if (pg.mouse.get_pos()[0] >= 440) and (pg.mouse.get_pos()[0] <= 490):
			if (pg.mouse.get_pos()[1] >= 12) and (pg.mouse.get_pos()[1] <= 80):
				show_planet = showBar(show_bar,"Nepture",neptune_gif)

		print(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
		'''
		if flag_mercury:
			show_planet = showBar(show_bar,"Mercury",mercury_gif)
		if flag_venus:
			show_planet = showBar(show_bar,"Venus",venus_gif)
		if flag_earth:
			show_planet = showBar(show_bar,"Earth",earth_gif)
		'''
		

	if pause == False: 
		# draw the earth
		earth_x,earth_y = cur_pos(sun_x,sun_y-earth_orb_r,earth_period,earth_orb_r) 
		# print(earth_x,earth_y)
		# pg.draw.circle(window,pg.Color("blue"),(int(round(earth_x,0)),int(round(earth_y,0))),earth_r,0)
		orb_list.append([earth_x,earth_y])

		# increment the count value
		count += 1

		# draw the orbital
		# pg.draw.circle(window,pg.Color("gray"),(sun_x,sun_y),earth_orb_r,1) # permanent orbital
		for i in range(0,len(orb_list)):
			pg.draw.rect(window,pg.Color("white"),(orb_list[i][0],orb_list[i][1],8,8),0)

		if len(orb_list) == 100:
			orb_list.pop(0)

		if earth_index == 5:
			earth_index = 0
		earth_curgif = earth_gif[earth_index]
		window.blit(earth_curgif,(earth_x-earth_r,earth_y-earth_r))
		earth_index += 1

		# relationship between the velocity and radius
		# value_x = (((slider_x-28 ) * max_v)  / slider_length) + min_v

		# initialise acceleration
		acc = ((const_G*mass_sun)/((earth_orb_r*(10**9))**2))*10**(-3) # km/s^2

		if value_x > true_v:
			value_x = value_x + acc*del_t 
			earth_orb_r = earth_orb_r + value_x*del_t
		elif value_x < true_v:
			value_x = value_x - acc*del_t
			earth_orb_r = earth_orb_r - value_x*del_t
			
		slider2_x = (((earth_orb_r - min_radius) /(max_radius-min_radius))*slider_length)+300

		# print(acc)
		# print(value_x)
		# print(earth_orb_r)
	# if it collides with the sun
	if rect_collide(400,400,sun_r,earth_x,earth_y,earth_r):
		pg.draw.rect(window,pg.Color("Gray"),(270,320,260,150),0)
		pause = True

		text_collide1 = font.render("You have collided...",True,(0,0,0))
		text_collide2 = font.render("With the Sun!!",True,(0,0,0)) # antialias - smooth curves
		window.blit(text_collide1,(300,350))
		window.blit(text_collide2,(300,400))

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
	window.blit(tb_pause,(620,12))
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
