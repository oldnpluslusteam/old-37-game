# coding=UTF-8
from fwk.game.game import *
from fwk.util.all import *
from fwk.ui.layers.gameLayer import GameLayer as GameLayer_

import arrows

_NUM_ARROWS = 100
_FIRST_ARROW_POS = (0, 200)
_BG_RANGE_X = (-3, 4)
_BG_RANGE_Y = (-3, 4)
_BG_IMAGE = LoadTexture('rc/img/fon.png')

_bg_positions = [(a, b) for a in range(*_BG_RANGE_X) for b in range(*_BG_RANGE_Y)]


class OuterGame(Game):
    def __init__(self, sstate):
        Game.__init__(self)
        self._sstate = sstate
        self.addEntity(arrows.OuterGlobalArrow.make_initial(_FIRST_ARROW_POS, _NUM_ARROWS))
        self._bg_sprites = zip(_bg_positions, [self.createSprite(_BG_IMAGE, -200) for _ in _bg_positions])
        self._bg_sizes = (self._bg_sprites[0][1].width, self._bg_sprites[0][1].height)

    @property
    def sstate(self):
        return self._sstate

    def update(self, dt):
        px, py = self.getEntityById('player').position
        sx, sy = self._bg_sizes
        cx, cy = px // sx, py // sy

        for off, spr in self._bg_sprites:
            ox, oy = off
            spr.x = (cx + ox) * sx
            spr.y = (cy + oy) * sy

    def drawSprites(self):
        Game.drawSprites(self)


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
