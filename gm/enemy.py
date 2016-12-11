# coding=UTF-8
from fwk.game.entity import GameEntity
from gm.mixins import *


class Enemy(GameEntity, GameEntity.mixin.Sprite, Collidable):

	def spawn(self):
		self.sprite = 'rc/img/32x32fg.png'
		self.addTags('enemy')

	def update(self, dt):
		self.game.getEntityById('player')