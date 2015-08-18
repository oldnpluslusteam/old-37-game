#!/usr/bin/python
# coding=UTF-8

from fwk.ui.screen import Screen
from fwk.ui.console import GAME_CONSOLE

from fwk.ui.layers.staticBg import StaticBackgroundLauer
from fwk.ui.layers.guiItem import GUIItemLayer
from fwk.ui.layers.guitextitem import GUITextItem
from fwk.ui.layers.gameLayer import GameLayer
from fwk.ui.layers.texture9TileItem import *

from fwk.game.game import Game
from fwk.game.entity import GameEntity
from fwk.game.camera import Camera

import fwk.sound.static as ssound
import fwk.sound.music as music

from fwk.util.all import *

@GameEntity.defineClass('test-entity')
class TestEntity(GameEntity):
	def spawn(self):
		print 'TestEntity:spawn()'
		self.think()

	def think(self):
		print 'TestEntity:think()'
		self.game.scheduleAfter(1.0,self.think)

@Screen.ScreenClass('STARTUP')
class StartupScreen(Screen):
	def init(self,*args,**kwargs):

		self.pushLayerFront(StaticBackgroundLauer('rc/img/256x256bg.png','fill'))

		game = Game()
		camera = Camera()

		game.loadFromJSON('rc/lvl/level0.json')

		self.pushLayerFront(GameLayer(game=game,camera=camera))

		ssound.Preload('rc/snd/1.wav',['alias0'])

		musmap = {0:'rc/snd/music/Welcome.mp3',1:'rc/snd/music/Time.mp3',2:'rc/snd/music/0x4.mp3'}

		for x in xrange(0,3):
			layer = GUITextItem(
				layout={
					'width':100,
					'height':20,
					'left':50,
					'right':50,
					'offset_y':70*x,
					'padding':[20,10],
					'force-size':False
					},
				text=musmap[x]);
			layer.on('ui:click',(lambda x: lambda *a: music.Play(musmap[x],loop=True))(x))
			self.pushLayerFront(layer)

		tile = _9Tiles(LoadTexture('rc/img/ui-frames.png'),Rect(left=0,bottom=0,width=12,height=12))

		self.pushLayerFront(GUI9TileItem(
			tiles=tile,
			layout = {
				'left': 100,
				'right': 100,
				'top': 200,
				'bottom': 200
			}))

		GAME_CONSOLE.write('Startup screen created.')

	def on_key_press(self,key,mod):
		pass#GAME_CONSOLE.write('SSC:Key down:',KEY.symbol_string(key),'(',key,') [+',KEY.modifiers_string(mod),']')
