#!/usr/bin/python
# coding=UTF-8

from fwk.ui.screen import Screen
from fwk.ui.console import GAME_CONSOLE

from fwk.game.camera import Camera

from gm.outer_game import *
from gm.inner_game import *
from gm.shr import *

from fwk.util.all import *

from gm.progress_bar import ProgressBar


@Screen.ScreenClass('STARTUP')
class StartupScreen(Screen):
    def _setup_progress_bars(self, sstate):
        self.pushLayerFront(ProgressBar(
            grow_origin='top-left',
            expression=lambda: sstate.get_stat('energy'),
            layout={'height': 20, 'width': 300, 'top': 50, 'right': 50}
        ))
        self.pushLayerFront(ProgressBar(
            grow_origin='top-left',
            expression=lambda: sstate.get_stat('hp-xyz'),
            layout={'height': 20, 'width': 300, 'top': 80, 'right': 50}
        ))
        self.pushLayerFront(ProgressBar(
            grow_origin='top-left',
            expression=lambda: sstate.get_stat('hp-rust'),
            layout={'height': 20, 'width': 300, 'top': 110, 'right': 50}
        ))

    def init(self, *args, **kwargs):
        # self.pushLayerFront(StaticBackgroundLauer('rc/img/256x256bg.png','fill'))

        sgs = SharedGameState()

        ogame = OuterGame(sgs)
        ogame.loadFromJSON('rc/lvl/level-outer.json')

        ocamera = Camera()

        igame = InnerGame(sgs)
        igame.loadFromJSON('rc/lvl/level-inner.json')

        icamera = Camera()

        self.pushLayerFront(OuterGameLayer(game=ogame, camera=ocamera))
        self.pushLayerFront(InnerGameLayer(game=igame, camera=icamera))

        self._setup_progress_bars(sgs)

        GAME_CONSOLE.write('Startup screen created.')

    def on_key_press(self, key, mod):
        pass  # GAME_CONSOLE.write('SSC:Key down:',KEY.symbol_string(key),'(',key,') [+',KEY.modifiers_string(mod),']')
