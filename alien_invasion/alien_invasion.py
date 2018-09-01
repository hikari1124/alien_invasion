import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# 创建Play按钮
	play_button = Button(ai_settings,screen,"Play")
	
	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	
	# 创建一个显示计分的实例
	sb = Scoreboard(ai_settings,screen,stats)
	
	# 创建一艘飞船
	ship = Ship(ai_settings,screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	# 创建一个外星人编组
	aliens = Group()
	#创建外星人群
	gf.creat_fleet(ai_settings,screen,ship,aliens)
	
	
	# 开始游戏的主循环
	while True:
		
		# 监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,aliens,bullets,stats,play_button)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,ship,aliens,bullets,sb)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
			
		# 每次循环都重绘屏幕,让最近绘制的屏幕可见
		gf.update_screen(ai_settings,screen,stats,ship,aliens,
			bullets,play_button,sb)
		
run_game()
