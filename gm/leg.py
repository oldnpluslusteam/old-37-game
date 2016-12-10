#encoding=UTF-8
from fwk.game.entity import GameEntity

class Leg(GameEntity, GameEntity.mixin.Animation, GameEntity.mixin.Attached):
	pass
	#
    # @property
    # def parent(self):
    #     return self._parent
	#
    # @parent.setter
    # def parent(self, parent_id):
    #     new_parent = self.game.getEntityById(parent_id)
    #     self.attach(new_parent)
