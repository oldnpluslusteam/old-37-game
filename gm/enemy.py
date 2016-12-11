# coding=UTF-8
from fwk.game.entity import GameEntity
from fwk.game.entity_mixin import Animation
from gm.mixins import *


class Enemy(GameEntity, Animation, Collidable):

	def spawn(self):
		self.animations = 'rc/ani/dog_anim.json'

	def update(self, dt):
		self.game.getEntityById('player')