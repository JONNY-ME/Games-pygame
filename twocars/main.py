import pygame
import random
import time

pygame.init() #initialize pygame


screen = pygame.display.set_mode((200, 600)) #game size
pygame.display.set_caption('Two Cars')    #title
icon = pygame.image.load('image/icon.png') # load icon
pygame.display.set_icon(icon)   # set icon to the game 
font = pygame.font.SysFont('Comic Sans MS', 23)

obb = pygame.image.load('image/obb.png')
obr = pygame.image.load('image/obr.png')
fdb = pygame.image.load('image/fdb.png')
fdr = pygame.image.load('image/fdr.png')
crr = pygame.image.load('image/crr.png')
crb = pygame.image.load('image/crb.png')

def draw_obb(x, y):
	screen.blit(obb, (x, y))
def draw_obr(x, y):
	screen.blit(obr, (x, y))
def draw_fdb(x, y):
	screen.blit(fdb, (x, y))
def draw_fdr(x, y):
	screen.blit(fdr, (x, y))

def generate_next_blue(blues):
	b = blues.copy()
	b.append([random.choice([7, 57]), 0, random.choice([0, 1])])
	return b
def generate_next_red(reds):
	r = reds.copy()
	r.append([random.choice([107, 157]), 0, random.choice([0, 1])])
	return r
def draw_thing(s, x, y):
	screen.blit(font.render(s, False, (255, 255, 255)), (x, y))

drr = [7, 57, 107, 157]
xb = drr[0]
xr = drr[3]
yb = yr = 520
red = generate_next_red([])
blue = generate_next_blue([])
speed = .1
running = True
score = None 
high_score = 0
playing = False 

while running:
	screen.fill((0, 0, 0))

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if (event.key == 1073741918 or event.key == pygame.K_d) and playing:
				xr = drr[-2:][xr == drr[2]]
			elif (event.key == 1073741916 or event.key == pygame.K_a) and playing:
				xb = drr[:2][xb == drr[0]]
			elif event.key == pygame.K_s:
				playing = True
				xb = drr[0]
				xr = drr[3]
				yb = yr = 520
				red = generate_next_red([])
				blue = generate_next_blue([])
				speed = .1
				score = 0 


	if playing:

		# adding next fd or ob 
		if blue[-1][1] > 120 + 20*random.random():
			blue = generate_next_blue(blue)
		if red[-1][1] > 120 + 20*random.random():
			red = generate_next_red(red)



		bac_red = []
		for i in range(len(red)):
			if red[i][1] < 600:
				bac_red.append([red[i][0], red[i][1]+speed, red[i][2]])
		red = bac_red

		bac_blue = []
		for i in range(len(blue)):
			if blue[i][1] < 600:
				bac_blue.append([blue[i][0], blue[i][1]+speed, blue[i][2]])
		blue = bac_blue


		if abs(red[0][1] - yr) <= 20 and xr == red[0][0]:
			if red[0][2] == 1:
				red = red[1:]
				if score == None:
					score = 1 
				else:
					score += 1
			else:
				playing = False

		if abs(blue[0][1] - yb) <= 20 and xb == blue[0][0]:
			if blue[0][2] == 1:
				blue = blue[1:]
				if score == None:
					score = 1 
				else:
					score += 1
			else:
				playing = False
		if red[0][1] > 545 and red[0][2]:
			playing = False
		if blue[0][1] > 545 and blue[0][2]:
			playing = False

		pygame.draw.rect(screen, (173,216,230), (50, 0, 2, 600))
		pygame.draw.rect(screen, (173,216,230), (100, 0, 2, 600))
		pygame.draw.rect(screen, (173,216,230), (150, 0, 2, 600))
		screen.blit(crb, (xb, yb))
		screen.blit(crr, (xr, yr))
		for x, y, t in red:
			if t == 1:
				draw_fdr(x, y)
			else:
				draw_obr(x, y)
		for x, y, t in blue:
			if t == 1:
				draw_fdb(x, y)
			else:
				draw_obb(x, y)
		if score == None:
			score = 0 
		draw_thing(str(score), 157, 0)
		speed +=0.000005
	else:
		if score == None:
			draw_thing('press s to start new game', 0, 150)
		else:
			pygame.draw.rect(screen, (173,216,230), (50, 0, 2, 600))
			pygame.draw.rect(screen, (173,216,230), (100, 0, 2, 600))
			pygame.draw.rect(screen, (173,216,230), (150, 0, 2, 600))
			screen.blit(crb, (xb, yb))
			screen.blit(crr, (xr, yr))
			for x, y, t in red:
				if t == 1:
					draw_fdr(x, y)
				else:
					draw_obr(x, y)
			for x, y, t in blue:
				if t == 1:
					draw_fdb(x, y)
				else:
					draw_obb(x, y)
			high_score = max(high_score, score)
			draw_thing(f'your score = {score}', 40, 150)
			draw_thing(f'high score = {high_score}', 40, 220)
			draw_thing('press s to start new game', 0, 300)


	
	
	pygame.display.update()