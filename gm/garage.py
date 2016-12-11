# coding=utf-8
from fwk.game.entity import GameEntity
from gm.leg import Leg

from fwk.util.all import *

_K_ENERGY = 3.
_K_ANGULAR = 10.
_K_LINEAR = 50


@GameEntity.defineClass('outer:player')
class Garage(GameEntity, GameEntity.mixin.Sprite, GameEntity.mixin.CameraTarget, GameEntity.mixin.Movement):
	z_index=5

	def spawn(self):
		self._attach_events = ['update', 'delete'] # без этого не работает

		left_leg = Leg()
		self.game.addEntity(left_leg)
		left_leg.attach(self)
		left_leg.animations = "rc/ani/noga_left_anim.json"
		left_leg.animation = 'walk'
		left_leg.side = 'left'
		self._ll = left_leg

		right_leg = Leg()
		self.game.addEntity(right_leg)
		right_leg.attach(self)
		right_leg.animations = "rc/ani/noga_right_anim.json"
		right_leg.animation = 'walk'
		right_leg.side = 'right'
		self._rl = right_leg

	def update(self, dt):
		# Определённо, это один из самых жестоких способов перемещения игрока, что мне когда-либо приходилось писать.
		if self._rl.isMoving() or self._ll.isMoving():
			ke = self.game.sstate.get_stat('energy') * _K_ENERGY
			ka = (ke if self._ll.isMoving() else 0) - (ke if self._rl.isMoving() else 0)
			kl = (ke if self._rl.isMoving() else 0) + (ke if self._ll.isMoving() else 0)
			self.angularVelocity = ka * _K_ANGULAR
			dx, dy = directionFromAngle(self.rotation)
			self.velocity = (_K_LINEAR * dx * kl, _K_LINEAR * dy * kl)
		else:
			self.angularVelocity = 0
			self.velocity = (0,0)

	def do(self, leg, action):
		getattr(getattr(self, '_{0}l'.format(leg)), 'do{0}'.format(action))()
