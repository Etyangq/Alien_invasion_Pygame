
import pygame
from pygame.sprite import Group


from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	"""初始化游戏并创建一个屏幕对象"""
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建一个用于储存游戏统计信息的实例
	stats = GameStats(ai_settings)

	#创建储存游戏统计信息的实例,并创建记分牌
	sb = Scoreboard(ai_settings, screen, stats)

	#创建一艘飞船
	ship = Ship(ai_settings, screen)
	
	#创建一个用于储存外星人的空编组
	aliens = Group()

	#创建一个用于储存子弹的编组
	bullets = Group()

	


	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
   
	#创建Play按钮
	play_button = Button(ai_settings, screen, "Play")

	#开始游戏主循环
	while True:
		filename = 'high_score.txt'
		with open(filename, 'w') as file_object:
			file_object.write(str(stats.high_score))

		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen,stats, sb, ship, aliens, bullets, play_button)

run_game() 