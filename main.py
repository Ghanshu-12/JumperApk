from kivymd.app import MDApp
from kivymd.utils import asynckivy
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.vector import *
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
Window.size=(360,669)
class JumpuGameApp(MDApp):
    def build(self):
        global sm
        self.score=0
        sm=ScreenManager()
        sm.add_widget(Builder.load_file('main.kv'))
        sm.add_widget(Builder.load_file('menu.kv'))
        self.ball=sm.get_screen('main').ids.ball
        self.wall=sm.get_screen('main').ids.wall
        self.set_heading()
        self.down_ball()
        return sm
    def set_heading(self):
        async def set_heading():
            while True:
                self.score+=1
                await asynckivy.sleep(1)
                text_h=sm.get_screen('main').ids.score
                text_h.text=f'Score:-{str(self.score)}'
        asynckivy.start(set_heading())
    def down_ball(self):
        async def down_ball():
            while True:
                self.ball.pos[1]-=10
                if self.ball.pos==self.wall.pos:
                    sm.current='menu'
                    sm.get_screen('menu').ids.finalscore.text=f'Final Score:-{self.score-1}'
                await asynckivy.sleep(.1)
        asynckivy.start(down_ball())
    def upball(self,ball):
        ball.pos[1]+=20
    def hm(self):
        sm.current='main'
        self.ball.pos=20,300
        self.score=0
root=JumpuGameApp()
root.run()