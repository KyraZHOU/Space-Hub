import pygame as pg 

pg.init()
screen = pg.display.set_mode((800,800)) # size of the screen
pg.display.set_caption("Gravitational Field")


# Set up background
background = pg.image.load('bg3.jpeg').convert()
# Set up button
startButton = pg.image.load('sb.png')
flashLight = pg.image.load('fl.png')

def drawText(text,x,y,textHeight=30,fontColor=(255,255,255),backgroudColor=(0,0,0),fontType="font.ttf"):
	# Set the font of the text
	font = pg.font.Font(fontType, textHeight)
	textCont = font.render(text, True,fontColor,backgroudColor)
	textPos = textCont.get_rect() 
	textPos.center = (x,y)

	return textCont,textPos

run = True
while run:
	# Display the moving flashLight
	x, y = pg.mouse.get_pos()
	x-= flashLight.get_width() / 2
	y-= flashLight.get_height() / 2

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

	screen.fill((0,0,0)) # black window

	# Display background
	screen.blit(background,(0,0))

	# Display button
	screen.blit(startButton,(300,600))

	# Draw Title
	title1_cont,title1_pos = drawText("Space",400,180,textHeight = 90)
	screen.blit(title1_cont,title1_pos) 
	title2_cont,title2_pos = drawText("HUB",400,280,textHeight = 76)
	screen.blit(title2_cont,title2_pos)

	# Display flash flight
	screen.blit(flashLight, (x, y))

	# update
	pg.display.update()
pg.quit()