# coding=UTF-8
from fwk.game.entity import GameEntity
from gm.mixins import *


class Enemy(GameEntity, GameEntity.mixin.Animation, Collidable):

	def spawn(self):
		self.animations = 'rc/ani/dog_anim.json'
		self.animation = 'walk'
		self.scale = 0.5
		self.addTags('enemy')

	def update(self, dt):
		self.game.getEntityById('player')