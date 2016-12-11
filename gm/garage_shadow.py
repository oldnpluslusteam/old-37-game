# coding=utf-8
from fwk.game.entity import GameEntity

from fwk.util.all import *

class GarageShadow(GameEntity, GameEntity.mixin.Animation, GameEntity.mixin.Attached):
	def doStep(self):
		self.animation = 'walk'
		self.game.scheduleAfter(1, lambda : setattr(self, 'animation','stand'))

	def doAttack(self):
		self.animation = 'attack'
		self.game.scheduleAfter(1, lambda : setattr(self, 'animation','stand'))