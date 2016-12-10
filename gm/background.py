# encoding=UTF-8
from fwk.game.entity import GameEntity


@GameEntity.defineClass('outer:background')
class Background(GameEntity, GameEntity.mixin.Sprite):
	z_index = -1
