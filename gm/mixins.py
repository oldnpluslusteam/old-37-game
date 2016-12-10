# coding=UTF-8
"""
Модуль содержит набор классов-примесей который ещё не "опробованы временем" (с)
"""

from fwk.util.geometry import *

COLLIDABLE_ENTITY_TAG = 'collidables'
COLLIDABLE_ACTION_NAME = 'collide'

class Collidable:
	'''
	Примесь, добавляющая коллизии для окружностей
	'''

	def spawn(self):
		self.addTags(self, [COLLIDABLE_ENTITY_TAG])
		self._size = 0

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, new_size):
		self.size = new_size

	def update(self, dt):
		other_collidables  = self.game.getEntitiesByTag(COLLIDABLE_ENTITY_TAG)

		for other_collidable in other_collidables:
			if self.is_collide(other_collidable):
				self.trigger_collision(other_collidable)

	def is_collide(self, other_collidable):
		dist = distance(self.position, other_collidable.position)
		r_sum = self.size + other_collidable.size()
		return dist < r_sum

	def trigger_collision(self, other_collidable):
		self.trigger(COLLIDABLE_ACTION_NAME, other_collidable)
		other_collidable.trigger(COLLIDABLE_ACTION_NAME, self)
