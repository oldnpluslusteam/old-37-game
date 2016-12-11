# coding=utf-8
from fwk.game.entity import GameEntity
import random as rnd

from fwk.util.all import *

_ANGLE_DELTA = 45.
_DIST_MIN = 300
_DIST_MAX = 500


@GameEntity.defineClass('outer:globalArrow')
class OuterGlobalArrow(GameEntity, GameEntity.mixin.Sprite):
    z_index = -50

    @staticmethod
    def make_initial(pos, depth):
        arrow = OuterGlobalArrow()
        arrow.position = pos
        arrow._depth = depth
        return arrow

    def spawn(self):
        self._generate_next()
        self.sprite = 'rc/img/arrow-global.png'

    def _generate_next(self):
        if self._depth == 0:
            t = FinalDestination()
            self.game.addEntity(t)
            t.position = self.position
            return

        next_arrow = OuterGlobalArrow()

        a = rnd.uniform(-45, 45) + self.rotation
        dst = rnd.uniform(_DIST_MIN, _DIST_MAX)
        dx, dy = directionFromAngle(self.rotation)
        x0, y0 = self.position
        next_arrow._depth = self._depth - 1
        next_arrow.position = (x0 + dx * dst, y0 + dy * dst)
        next_arrow.rotation = a

        self.game.addEntity(next_arrow)


@GameEntity.defineClass('outer:fd')
class FinalDestination(GameEntity, GameEntity.mixin.Sprite):
    z_index = -40

    def spawn(self):
        self.sprite = 'rc/img/32x32fg.png'

