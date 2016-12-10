# encoding=UTF-8
from fwk.game.entity import GameEntity

_STEP_DURATION = 1.


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

    def doAttack(self):
        pass

    def isMoving(self):
        return self._state == 'step'
