# encoding=UTF-8
from fwk.game.entity import GameEntity
from fwk.util.geometry import *
from gm.hurter import Hurter

_STEP_DURATION = 1.
_STEP_EFFECT = {'energy': '{0}*0.99'}

class Leg(GameEntity, GameEntity.mixin.Animation, GameEntity.mixin.Attached):
    def spawn(self):
        self._go_to_idle()

    def _go_to_idle(self):
        self._state = 'idle'
        self.animation = 'stand'

    def doStep(self):
        if self._state != 'idle':
            return

        self._state = 'step'
        self.animation = 'walk'
        self.game.scheduleAfter(_STEP_DURATION, self._go_to_idle)
        self.game.sstate.apply_effects(_STEP_EFFECT)

    def doAttack(self):
        attack_shift = 200
        x_, y_ = perpendicularDirection(directionFromAngle(self.rotation))
        if self.side == 'left':
            x_ = -x_
            y_ = -y_
        h_pos = map(lambda pos, pos_: pos_*attack_shift+pos, self.position, (x_, y_))
        hurter = Hurter.static_init(self.game, self, h_pos, (0, 0), 200, 0, 10, 'bash', 'enemy')

    def isMoving(self):
        return self._state == 'step'
