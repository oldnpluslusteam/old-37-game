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
class InnerPlayer(GameEntity, Sprite, CameraTarget, Movement):
    def spawn(self):
        self._v_fwd = self._v_lf = self._v_rt = self._v_back = 0

_KDICT = {KEY.W: '_v_fwd', KEY.A: '_v_lf', KEY.S: '_v_back', KEY.D: '_v_rt'}

class InnerGameLayer(GameLayer_):
    def init(self, *args, **kwargs):
        self._player = self._game.getEntityById('player')
        self._camera.focus = (0, 0)

    def on_key_press(self, key, mod):
        if key in _KDICT:
            setattr(self._player, _KDICT[key], 1)
        if key == KEY.E:
            pass

    def on_key_release(self, key, *args):
        if key in _KDICT:
            setattr(self._player, _KDICT[key], 0)

    def draw(self):
        GameLayer_.draw(self)
