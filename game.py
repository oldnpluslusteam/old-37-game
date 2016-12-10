#!/usr/bin/python
# coding=UTF-8

from fwk.ui.screen import Screen
from fwk.ui.console import GAME_CONSOLE

from fwk.ui.layers.staticBg import StaticBackgroundLauer
from fwk.ui.layers.guiItem import GUIItemLayer
from fwk.ui.layers.guitextitem import GUITextItem
from fwk.ui.layers.gameLayer import GameLayer as GameLayer_
from fwk.ui.layers.texture9TileItem import *

from fwk.game.game import Game
from fwk.game.entity import GameEntity
from fwk.game.camera import Camera

import fwk.sound.static as ssound
import fwk.sound.music as music

from gm.outer_game import *
from gm.inner_game import *
from gm.shr import *

from fwk.util.all import *


@Screen.ScreenClass('STARTUP')
class StartupScreen(Screen):
	def init(self,*args,**kwargs):

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

		GAME_CONSOLE.write('Startup screen created.')

	def on_key_press(self,key,mod):
		pass#GAME_CONSOLE.write('SSC:Key down:',KEY.symbol_string(key),'(',key,') [+',KEY.modifiers_string(mod),']')
