from kivy.app import App
from kivy.uix.button import Button

class DartApp(App):
    def build(self):
        return Button(text='Hello World')

DartApp().run()