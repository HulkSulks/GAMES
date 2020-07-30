#IMPORTING PYGAME RANDOM AND SYSTEM
import pygame
import random
import sys

#INITIALIZING PYGAME
pygame.init()

#HEIGHT AND WIDTH OF THE SCREEN
WIDTH = 800
HEIGHT = 600

#COLOR CODES(R, G, B)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,0,0)

#PLAYER INFO
player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

#ENEMY CODES
enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]
#SPEED OF ENEMY
SPEED = 10

#DEFINING THE SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#GAME OVER SET TO FALSE TO START THE GAME
game_over = False

#SCORE SET TO 0 WHEN START
score = 0

#pygame.time.clock() IS USED TO DEFINE A FRAME RATE
clock = pygame.time.Clock()

myFont = pygame.font.SysFont("verdana", 35)

def set_level(score, SPEED):
	if score < 20:
		SPEED = 5
	elif score < 40:
		SPEED = 8
	elif score < 60:
		SPEED = 12
	else:
		SPEED = 15
	return SPEED
	# SPEED = score/5 + 1

#FUNCTION TO DROP ENEMY BLOCKS
def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

#FUNCTION TO DRAW THE ENEMIES
def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

#FUNCTION TO CHANGE ENEMY POSITION EVERY TIME THEY FALL AND ALSO INCREASE SPEED
def update_enemy_positions(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED
		else:
			enemy_list.pop(idx)
			score += 1
	return score

#CHECKING FOR ANY POSSIBLE COLLISIONS
def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

#IF ANY COLISSIONS PYTHON DETECTS
def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]
    #IF ENEMY(X) IS MORE THAN PLAYER(X) AND ENEMY(X) IS LESS THAN PLAYER(X) + IT'S SIZE (OR) PLAYER(X) IS MORE THAN ENEMY(X) AND PLAYER(X) IS LESS THAN ENEMY(X) + IT'S SIZE
	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		#OR ENEMY(Y) IS MORE THAN PLAYER(Y) AND ENEMY(Y) IS LESS THAN PLAYER(Y) + IT'S SIZE (OR) PLAYER(Y) IS MORE THAN ENEMY(Y) AND PLAYER(Y) IS LESS THAN ENEMY(Y) + IT'S SIZE
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False

#WHILE THE GAME IS NOT YET OVER
while not game_over:
    
	#IF THE EVENT GIVEN BY THE USER IS QUITTING THE WINDOW THE SYS MODULE EXITS THE PYGAME WINDOW
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
        
		#KEY PRESS CLASS IN PYGAME
		if event.type == pygame.KEYDOWN:
             
			#PLAYER POSITIONS IN X & Y CORDINATES
			x = player_pos[0]
			y = player_pos[1]
            
			#IF PLAYER PRESSES LEFT KEY THE PLAYER WILL MOVE 1 TIME IT'S OWN SIZE
			if event.key == pygame.K_LEFT:
				x -= player_size
		    
			#ELSE IF PLAYER PRESSES RIGHT KEY THE PLAYER WILL MOVE 1 TIME IT'S OWN SIZE
			elif event.key == pygame.K_RIGHT:
				x += player_size
            
			#AFTER MOVING THE PLAYER POSITION VARIABLE IS UPDATED TO X,Y IN THE ABOVE LINES
			player_pos = [x,y]
     
	#THE DISPLAY OF THE GAME IS SET TO BLACK
	screen.fill(BACKGROUND_COLOR)
    
	#DEFINING THE CONDITIONS IN THE FUNCTIONS OF THE ABOVE LINES
	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	SPEED = set_level(score, SPEED)
    
	#SCORE IS WRITTEN
	text = "Score:" + str(score)
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH-200, HEIGHT-40))
    
	#IF ENEMY COLLIDES THE PLAYER IT'S GAMEOVER!
	if collision_check(enemy_list, player_pos):
		game_over = True
		break

	draw_enemies(enemy_list)

	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

	#FRAME PER SECOND(FPS) IS SET TO 30 
	clock.tick(30)

	pygame.display.update()
