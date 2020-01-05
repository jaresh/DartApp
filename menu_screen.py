from kivy.app import App
from kivy.uix.screenmanager import Screen

class MenuScreen(Screen):
    def stop(self):  # pylint: disable=no-self-use
        App.get_running_app().stop()
