import pygame
import random
import time

pygame.init() #initialize pygame


screen = pygame.display.set_mode((800, 600)) #game size
pygame.display.set_caption('game by jo')    #title
icon = pygame.image.load('images/48.png') # load icon
pygame.display.set_icon(icon)   # set icon to the game 
font = pygame.font.SysFont('Comic Sans MS', 50)


win_text = font.render('You Win', False, (124, 0, 124))
start_new = font.render('press s to start new game', False, (124, 0, 124))


playerim = pygame.image.load('images/63.png')
px = 400
py = 520
cx = 0

enemyim = pygame.image.load('images/91.png')
def create_enemy():
	ex = fx = random.randint(0, 736)
	fy = ey = random.randint(20, 100)
	return ex, ey, fx, fy



def enemy(x, y):
	screen.blit(enemyim, (x, y))

def player(x, y):
	screen.blit(playerim, (x, y))

def fire(x, y):
	pygame.draw.rect(screen, (255, 0, 0), (x, y, 5, 12))

def random_dirc(x, y, dx, dy):
	if abs(x-dx)<4 and abs(y - dy)<4:
		dx = random.randint(0, 736)
		dy = random.randint(20, 100)
	if dx > x:
		x += .3
	elif dx < x:
		x -= .3
	if dy > y:
		y += .3
	elif dy < y:
		y -= .3
	return x, y, dx, dy

constant_nenemy = 15

n_enemy = constant_nenemy
enemies = [create_enemy() for i in range(n_enemy)]


fires = []
start = time.time()
xt = interval = .2
running = True
display_time = 1
while running:
	screen.fill((0, 0, 0))


	curr = time.time() - start
	if curr > display_time and n_enemy != 0:
		display_time += 1
	if curr >= interval:
		interval += xt
		fires.append([px+30, py-30])
	fire_backup = []
	for fr in fires:
		if fr[1] > 0:
			fire_backup.append(fr)
	fires = fire_backup
	skey = 0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				cx =- 1
			elif event.key == pygame.K_d:
				cx =+ 1
			elif event.key == pygame.K_s:
				skey = 1
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				cx = 0
	
	if px+cx >= 0 and px+cx < 736:
		px += cx

	player(px, py)

	
	en_bc = []
	for en in enemies:
		ex, ey, fx, fy = en
		enemy(ex, ey)
		en_bc.append(random_dirc(ex, ey, fx, fy))
	enemies = en_bc

	enemy_survived = [1 for _ in range(n_enemy)]
	fire_backup = []
	for i, j in fires:
		fire(i, j)
		fire_backup.append([i, j-1])
		for k in range(n_enemy):
			if abs(enemies[k][0] - i) + abs(enemies[k][1] - j) <= 16:
				enemy_survived[k] = 0
	fires = fire_backup
	
		
	
	en_bc = []
	for i in range(n_enemy):
		if enemy_survived[i]:
			en_bc.append(enemies[i])
	enemies = en_bc


	n_enemy = sum(enemy_survived)

	if n_enemy == 0:
		screen.fill((0, 0, 0))
		screen.blit(win_text,(200,280))
		screen.blit(start_new,(200,400))
		screen.blit(font.render(f'{display_time} seconds', False, (124, 0, 124)), (200, 500))
		if skey:
			n_enemy = constant_nenemy
			enemies = [create_enemy() for i in range(n_enemy)]
			start = curr 

	

	pygame.display.update()