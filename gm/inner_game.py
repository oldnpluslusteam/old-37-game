from fwk.game.entity import *
from fwk.game.entity_mixin import *
from fwk.game.game import *
from fwk.util.all import *
from fwk.ui.layers.gameLayer import GameLayer as GameLayer_

_SIZE_X_MIN = -100
_SIZE_X_MAX = 100
_SIZE_Y_MIN = -100
_SIZE_Y_MAX = 100
_PLAYER_VELOCITY = 200
_PLAYER_ANGLES = [
    7, 0, 1,
    6, 0, 2,
    5, 4, 3
]


class InnerGame(Game):
    def __init__(self, sstate):
        Game.__init__(self)
        self._sstate = sstate


@GameEntity.defineClass('inner:player')
class InnerPlayer(GameEntity, Sprite, CameraTarget, Movement):
    def spawn(self):
        self._v_fwd = self._v_lf = self._v_rt = self._v_back = 0
        self.animation = 'idle'

    def update(self, dt):
        dx = self._v_rt - self._v_lf
        dy = self._v_fwd - self._v_back
        self.velocity = (
            dx * _PLAYER_VELOCITY,
            dy * _PLAYER_VELOCITY
        )

        if dx != 0 or dy != 0:
            self.animation = 'walk'
            self.rotation = 45 * _PLAYER_ANGLES[(1 + dx) + 3 * (1 + dy)]
        else:
            self.animation = 'idle'

        x, y = self.position
        self.position = (
            max(_SIZE_X_MIN, min(_SIZE_X_MAX, x)),
            max(_SIZE_Y_MIN, min(_SIZE_Y_MAX, y))
        )


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
