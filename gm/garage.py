# coding=utf-8
from fwk.game.entity import GameEntity
from gm.leg import Leg


@GameEntity.defineClass('outer:player')
class Garage(GameEntity, GameEntity.mixin.Sprite, GameEntity.mixin.CameraTarget):
	z_index=5

	def spawn(self):
		self._attach_events = ['update', 'delete'] # без этого не работает

		left_leg = Leg()
		self.game.addEntity(left_leg)
		left_leg.attach(self)
		left_leg.animations = "rc/ani/noga_left_anim.json"
		left_leg.animation = 'walk'

		right_leg = Leg()
		self.game.addEntity(right_leg)
		right_leg.attach(self)
		right_leg.animations = "rc/ani/noga_right_anim.json"
		right_leg.animation = 'walk'


