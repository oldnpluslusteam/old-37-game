# coding=UTF-8
from fwk.game.game import *
from fwk.util.all import *
from fwk.ui.layers.gameLayer import GameLayer as GameLayer_

import arrows

_NUM_ARROWS = 100
_FIRST_ARROW_POS = (0, 200)


class OuterGame(Game):
    def __init__(self, sstate):
        Game.__init__(self)
        self._sstate = sstate
        self.addEntity(arrows.OuterGlobalArrow.make_initial(_FIRST_ARROW_POS, _NUM_ARROWS))

    @property
    def sstate(self):
        return self._sstate


class OuterGameLayer(GameLayer_):
    def init(self, *args, **kwargs):
        self._player = self._game.getEntityById('player')
        self._camera.setController(self._player)

    def on_key_press(self, key, mod):
        if key == KEY.NUM_4:
            self._player.do('l', 'Attack')
        if key == KEY.NUM_1:
            self._player.do('l', 'Step')
        if key == KEY.NUM_6:
            self._player.do('r', 'Attack')
        if key == KEY.NUM_3:
            self._player.do('r', 'Step')

    def draw(self):
        GameLayer_.draw(self)
