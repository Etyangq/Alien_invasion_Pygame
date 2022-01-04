class Settings():
	"""储存《外星人入侵》所有设置的类"""

	def __init__(self):
		"""初始化游戏的静态设置"""
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (22, 24, 35)

		#飞船设置
		self.ship_limit = 2

		#子弹设置
		self.bullet_width = 5
		self.bullet_height = 20
		self.bullet_color = (255, 0 , 0)
		self.bullets_allowed = 3

		#外星人设置
		self.fleet_drop_speed = 5

		#以什么样的速度加快游戏节奏
		self.speedup_scale = 1.1

		#外星人点数的提高速度
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 2
		self.alien_speed_factor = 0.5
		self.alien_points = 50

		#fleet_direction 为1表示向右边移动,为-1表示向左移
		self.fleet_direction = 1

	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)



		