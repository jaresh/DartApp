from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from menu_screen import MenuScreen
from player_screen import PlayerScreen
from match_screen import MatchScreen

Builder.load_file('layout.kv')

class DartApp(App):
    def __init__(self, **kwargs):
        super(DartApp, self).__init__(**kwargs)
        self.screen_m = ScreenManager()
        self.screen_m.add_widget(MenuScreen(name='menu'))
        self.screen_m.add_widget(PlayerScreen(name='player'))
        self.screen_m.add_widget(MatchScreen(name='match'))

    def build(self):
        return self.screen_m


DartApp().run()
