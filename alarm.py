import pygame
import time
import math

pygame.init()

screen = pygame.display.set_mode((500,600))

GREY = (120, 120, 120)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

font = pygame.font.SysFont('OPEN_SANS_BOLD', 50)

text_1 = font.render('+', True, BLACK)
text_2 = font.render('-', True, BLACK)
text_3 = font.render('+', True, BLACK)
text_4 = font.render('-', True, BLACK)
text_5 = font.render('Start', True, BLACK)
text_6 = font.render('Reset', True, BLACK)

total_secs = 0
total = 0
is_star = False
secs = 0
mins = 0
running = True

r_sec = 90
r_min 50

clock.pygame.time.Clock()

while running:
	clock.tick(60)
	screen.fill(GREY)
	sound = pygame.mixer.Sound('Alarm-ringtone.mp3') # You can change alarm ringtone if you want!
	
	mouse_x, mouse_y = pygame.mouse.get_pos();

	pygame.draw.rect(screen, WHITE, (100,50,50,50))
	pygame.draw.rect(screen,WHITE, (100,200, 50,50))
	pygame.draw.rect(screen,WHITE, (200,50, 50,50))
	pygame.draw.rect(screen,WHITE, (200,200, 50,50))
	pygame.draw.rect(screen, WHITE, (300,50, 150,50))
	pygame.draw.rect(screen,WHITE, (300,50,150,50))
	pygame.draw.rect(screen,WHITE, (300,150,150,50))

	screen.blit(text_1, (113,45))
	screen.blit(text_2, (115,200))
	screen.blit(text_3, (213,45))
	screen.blit(text_4, (215 ,200))
	screen.blit(text_5, (313,50))
	screen.blit(text_6, (313,150))


	pygame.draw.rect(screen,BLACK, (50,520, 400,50))
	pygame.draw.rect(screen,WHITE, (60,530, 380,30))

	pygame.draw.circle(screen, BLACK, (250,400), 100)
	pygame.draw.circle(screen, WHITE, (250,400), 95)
	pygame.draw.circle(screen, BLACK, (250,400), 5)

	pygame.draw.line(screen, BLACK, (250,400),(250,310))
	
	for event in pygame.event.get():
		if  event.type == pygame.QUIT:
			running = False
		if  event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pygame.mixer.pause()
				if:
					
			

	pygame.display.flip()

pygame.quit
# To be continued
