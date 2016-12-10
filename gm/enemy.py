# coding=UTF-8
from fwk.game.entity import GameEntity


class Enemy(GameEntity):

	def update(self, dt):
		self.game.getEntityById('player')