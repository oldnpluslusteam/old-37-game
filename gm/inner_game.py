from fwk.game.entity import *
from fwk.game.entity_mixin import *
from fwk.game.game import *
from fwk.util.all import *
from fwk.ui.layers.gameLayer import GameLayer as GameLayer_
import random

import item_types

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
_MIN_SELECT_DST = 50
_START_ITEMS = ['ogurezz'] * 4

class InnerGame(Game):
    def __init__(self, sstate):
        Game.__init__(self)
        self._sstate = sstate

        for _ in _START_ITEMS:
            sstate.items_queue.append(item_types.ITEMS[_])

    @property
    def sstate(self):
        return self._sstate

    def update(self, dt):
        if len(self.sstate.items_queue) != 0:
            ready_places = self.getEntitiesByTag('itemPlace')
            random.shuffle(ready_places)

            while len(self.sstate.items_queue) != 0 and len(ready_places) != 0:
                item = self.sstate.items_queue.pop()
                ready_places.pop().place(item)


@GameEntity.defineClass('inner:player')
class InnerPlayer(GameEntity, GameEntity.mixin.Animation, CameraTarget, Movement):
    def spawn(self):
        self._v_fwd = self._v_lf = self._v_rt = self._v_back = 0
        self.animation = 'idle'
        self._item = None

    def update(self, dt):
        dx = self._v_rt - self._v_lf
        dy = self._v_fwd - self._v_back
        self.velocity = (
            dx * _PLAYER_VELOCITY,
            dy * _PLAYER_VELOCITY
        )

        if dx != 0 or dy != 0:
            if self.animation != 'walk':
                self.animation = 'walk'
            self.rotation = 45 * _PLAYER_ANGLES[(1 + dx) + 3 * (1 - dy)]
        else:
            if self.animation != 'idle':
                self.animation = 'idle'

        x, y = self.position
        self.position = (
            max(_SIZE_X_MIN, min(_SIZE_X_MAX, x)),
            max(_SIZE_Y_MIN, min(_SIZE_Y_MAX, y))
        )

    def swap_item(self, item):
        i = self._item
        self._item = item
        return i


@GameEntity.defineClass('inner:itemPlace')
class InnerItemPlace(GameEntity, Sprite, Movement):
    def spawn(self):
        self.addTags('interactive', 'itemPlace')
        self._item = None
        self.angularVelocity = 100

    def place(self, item):
        if item is not None:
            self.sprite = item.sprite
            self.visible = True
        else:
            self.visible = False

        self._item = item

    @property
    def active(self):
        return self._item is not None

    def interact(self, player):
        self.place(player.swap_item(self._item))


@GameEntity.defineClass('inner:havalnik')
class InnerHavalnik(GameEntity, GameEntity.mixin.Animation):
    z_index = -1

    def spawn(self):
        self.animations = 'rc/ani/havalnik_anim.json'
        self.animation = 'stand'
        self.addTags('interactive')
        self.active = True

    def interact(self, player):
        it = player.swap_item(None)
        if it is not None:
            it.apply(self.game.sstate)
            print 'Amm', it


@GameEntity.defineClass('inner:hole')
class InnerHole(GameEntity, Sprite):
    def spawn(self):
        self.addTags('interactive')
        self.active = True

    def interact(self, player):
        it = player.swap_item(None)
        if it is not None:
            print 'Broken', it


@GameEntity.defineClass('inner:selector')
class InnerSelector(GameEntity, Sprite, Movement):
    def spawn(self):
        self._selected = None
        self.angularVelocity = 100

    def update(self, dt):
        ents = self.game.getEntitiesByTag('interactive')
        player = self.game.getEntityById('player')
        nearest = None
        nearest_d = _MIN_SELECT_DST * _MIN_SELECT_DST
        for e in ents:
            np = distance2(player.position, e.position)
            if np <= nearest_d:
                nearest_d = np
                nearest = e

        self.visible = nearest is not None
        self._selected = nearest

        if self._selected is not None:
            self.position = self._selected.position

    def act(self, player):
        if self._selected is not None:
            self._selected.interact(player)


_KDICT = {KEY.W: '_v_fwd', KEY.A: '_v_lf', KEY.S: '_v_back', KEY.D: '_v_rt'}


class InnerGameLayer(GameLayer_):
    def init(self, *args, **kwargs):
        self._player = self._game.getEntityById('player')
        self._camera.focus = (0, 0)

    def on_key_press(self, key, mod):
        if key in _KDICT:
            setattr(self._player, _KDICT[key], 1)
        if key == KEY.E:
            selector = self._game.getEntityById('selector')
            selector.act(self._player)

    def on_key_release(self, key, *args):
        if key in _KDICT:
            setattr(self._player, _KDICT[key], 0)

    def draw(self):
        GameLayer_.draw(self)
