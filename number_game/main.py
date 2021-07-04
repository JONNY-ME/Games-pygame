import pygame
import random
import time



def generate(seed=None):
	if seed != None:
		random.seed(seed)
	g = list(range(1, 10))
	s = ''
	for i in range(4):
		n = random.choice(g)
		g.remove(n)
		s += str(n)
	return s


def compare(a, b):
	p = 0
	n = 0
	for i in range(len(a)):
		if b[i] in a:
			n += 1
		if b[i] == a[i]:
			p += 1
	return str(n), str(p)

def draw_num(out, px, py):
	text = font.render(out, False, (0, 0, 0))
	screen.blit(text, (px, py))

num = generate()

pygame.init() #initialize pygame


screen = pygame.display.set_mode((800, 600)) #game size
pygame.display.set_caption('game by jo')    #title
#icon = pygame.image.load('.png') # load icon
#pygame.display.set_icon(icon)   # set icon to the game 
font = pygame.font.SysFont('Comic Sans MS', 45)


header = font.render('Number   Num     Pos', False, (0, 0, 0))
n_game1 = font.render('Enter  N', False, (0, 0, 0))
n_game2 = font.render('for new game', False, (0, 0, 0))

def win_lose(t, s):
	return font.render(f'You {t}    {s}', False, (0, 0, 0))

def draw_rect(x, y, lx, ly, cl):
	pygame.draw.rect(screen, cl, (x, y, lx, ly))

inx, iny = 300, 100
his = []
outstr = ''
trial = 0
win = 0
running = 1
start = time.time()
while running:
	screen.fill((0, 0, 0))


	draw_rect(250, 50, 400, 500, (173,216,230))
	draw_rect(20, 180, 200, 180, (216,173,230))
	screen.blit(header, (300, 50))
	screen.blit(n_game1, (20, 180))
	screen.blit(n_game2, (20, 220))
	pygame.draw.line(screen, (0, 0, 0), (420, 500), (420, 20))
	pygame.draw.line(screen, (0, 0, 0), (525, 500), (525, 20))
	pygame.draw.line(screen, (0, 0, 0), (260, 500), (800, 500))
	pygame.draw.line(screen, (0, 0, 0), (260, 90), (800, 90))

	# K_BACKSPACE  K_KP_ENTER
	num_pressed = ''
	enter_key = 0
	new_game = 0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1 or event.key == 1073741913:
				num_pressed = '1'
			elif event.key == pygame.K_2 or event.key == 1073741914:
				num_pressed = '2'
			elif event.key == pygame.K_3 or event.key == 1073741915:
				num_pressed = '3'
			elif event.key == pygame.K_4 or event.key == 1073741916:
				num_pressed = '4'
			elif event.key == pygame.K_5 or event.key == 1073741917:
				num_pressed = '5'
			elif event.key == pygame.K_6 or event.key == 1073741918:
				num_pressed = '6'
			elif event.key == pygame.K_7 or event.key == 1073741919:
				num_pressed = '7'
			elif event.key == pygame.K_8 or event.key == 1073741920:
				num_pressed = '8'
			elif event.key == pygame.K_9 or event.key == 1073741921:
				num_pressed = '9'
			elif event.key == pygame.K_BACKSPACE:
				outstr = outstr[:-1]
			elif event.key == pygame.K_n:
				new_game = 1
			elif event.key == 13 or event.key == pygame.K_KP_ENTER:
				enter_key = 1
			
			
		elif event.type == pygame.KEYUP:
			pass
	

	if num_pressed != '' and len(outstr)<4 and num_pressed not in outstr and not win and trial < 8:
		outstr += num_pressed
	
	elif enter_key and len(outstr)==4:
		val = compare(num, outstr)
		if sum([int(i) for i in val]) == 8:
			win = 1
		his.append([outstr, iny, val[0], val[1]])
		trial += 1
		iny += 50
		outstr = ''


	for out, py, nm, ps in his:
		pout = out + ' ' * 8 + nm + ' '*11 + ps + ' '
		draw_num(pout , inx, py)


	if win or trial == 8:
		if win:
			out_scr = win_lose('Win', num)
		else:
			out_scr = win_lose('Lose', num)
		screen.blit(out_scr, (300, 500))
	if new_game:
		num = generate()
		inx, iny = 300, 100
		his = []
		outstr = ''
		trial = 0
		win = 0

	draw_num(outstr, inx, iny)

	pygame.display.update()