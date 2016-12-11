# coding=UTF-8
from fwk.game.entity import GameEntity
from gm.mixins import *
from fwk.util.geometry import *
from math import atan2


def directionToAngle(pos):
    return radToDegree(atan2(pos[0], pos[1]))


_SPEED = 50


class Enemy(GameEntity, GameEntity.mixin.Movement, GameEntity.mixin.Animation, Collidable):
    def spawn(self):
        self.animations = 'rc/ani/dog_anim.json'
        self.animation = 'walk'
        self.scale = 0.5
        self.addTags('enemy')

    def update(self, dt):
        player = self.game.getEntityById('player')
        pos = map(lambda enemy_pos, player_pos: player_pos - enemy_pos, self.position, player.position)
        angle = directionToAngle(pos)
        self.rotation = angle
        vx, vy = directionFromAngle(angle)
        self.velocity = (vx * _SPEED, vy * _SPEED)
