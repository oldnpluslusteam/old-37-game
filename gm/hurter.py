# encoding=UTF-8
from fwk.game.entity import GameEntity
from gm.mixins import *


class Hurter(GameEntity, GameEntity.mixin.Movement, GameEntity.mixin.Sprite, Collidable):
	@staticmethod
	def static_init(game, owner, position, velocity, ttl, damage, radius, damage_type, enemy_tag):
		self = Hurter()
		game.addEntity(self)

		self.position = position
		self.velocity = velocity
		self.owner = owner
		self.damage = damage
		self.size = radius
		self.radius = radius
		self.damage_type = damage_type
		self.enemy_tag = enemy_tag
		game.scheduleAfter(ttl, self.destroy)
		self.sprite = "rc/img/32x32fg.png"
		self.scale = (self.radius / 16.0)
		self.on(COLLIDABLE_ACTION_NAME, self.hurter_collide, before=True)
		return self

	def hurter_collide(self, enemy):
		if enemy != self.owner and enemy in self.game.getEntitiesByTag(self.enemy_tag):
			self.do_damage(enemy)

	def do_damage(self, enemy):
		self.destroy()
