from fwk.game.entity import *
from fwk.game.entity_mixin import *
from fwk.game.game import *
from fwk.util.all import *
from fwk.ui.layers.gameLayer import GameLayer as GameLayer_


class InnerGame(Game):
    def __init__(self, sstate):
        Game.__init__(self)
        self._sstate = sstate


@GameEntity.defineClass('outer:player')
class InnerPlayer(GameEntity, Sprite, CameraTarget):
    pass


class InnerGameLayer(GameLayer_):
    def init(self, *args, **kwargs):
        self._player = self._game.getEntityById('player')
        self._camera.focus = (0, 0)

    def on_key_press(self, key, mod):
        if key == KEY.NUM_W:
            pass
        if key == KEY.NUM_A:
            pass
        if key == KEY.NUM_S:
            pass
        if key == KEY.NUM_D:
            pass
        if key == KEY.NUM_E:
            pass

    def draw(self):
        GameLayer_.draw(self)
