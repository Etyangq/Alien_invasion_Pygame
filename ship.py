import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		"""初始化飞船并设定其初始位置"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect() #表示元素的矩形
		self.screen_rect = screen.get_rect() #表示屏幕的矩形

		#将每艘飞船放在屏幕中央底部
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#在飞船属性center中存储小数值
		self.center = float(self.rect.centerx)

		#移动标志
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""根据移动标志调整飞船的位置"""
		#更新飞船的center值，而不是rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center

			
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		"""让飞船居中"""
		self.center= self.screen_rect.centerx
