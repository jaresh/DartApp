from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class DartApp(App):
    def __init__(self, **kwargs):
        super(DartApp, self).__init__(**kwargs)
        self.box = BoxLayout(orientation='horizontal', spacing=20)
        self.txt = TextInput(hint_text='Write here', size_hint=(.5, .1))
        self.btn = Button(text='Clear All', on_press=self.clear_text, size_hint=(.1, .1))

    def build(self):
        self.box.add_widget(self.txt)
        self.box.add_widget(self.btn)
        return self.box

    def clear_text(self, instance):  # pylint: disable=unused-argument
        self.txt.text = ''

DartApp().run()
