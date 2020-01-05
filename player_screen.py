from functools import partial
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from tinydb import TinyDB, Query

class PlayerDB():  # pylint: disable=too-few-public-methods
    def __init__(self):
        self.database = TinyDB('data/player.json')
        self.table = self.database.table('Player')
        self.query = Query()

    def get_names(self):
        names = []
        for player in self.table:
            names.append(player['name'])
        return names


class PlayerScreen(Screen):
    player_db = PlayerDB()

    def player_list_update(self):
        self.ids.player_list.clear_widgets()
        names = self.player_db.get_names()
        for name in names:
            print('name: %s' % name)
            label = Label(text=name, id="label_%s" % name)
            del_btn = Button(text='delete',
                             id="del_%s" % name,
                             on_press=partial(self.delete_player, name))
            stats_btn = Button(text='stats',
                               id="stats_%s" % name,
                               on_press=partial(self.stats_player, name))
            self.ids.player_list.add_widget(label)
            self.ids.player_list.add_widget(del_btn)
            self.ids.player_list.add_widget(stats_btn)

    def add_player(self, name):
        if self.player_db.table.get(self.player_db.query.name == name) is None:
            self.player_db.table.insert({'name': name, 'wins': 0})
        else:
            box = BoxLayout(orientation='vertical', padding=10)
            box.add_widget(Label(text='Name already used !'))
            btn1 = Button(text='Close window', size_hint_y=None, height=40)
            box.add_widget(btn1)

            popup = Popup(title='User not added', title_size=20,
                          title_align='center', content=box,
                          size_hint=(None, None), size=(200, 200),
                          auto_dismiss=False)
            btn1.bind(on_press=popup.dismiss)
            popup.open()

    def stats_player(self, name, instance):  # pylint: disable=unused-argument
        print("Names: %s" % self.player_db)  # Dumy for linting
        print("Stats: %s" % name)

    def delete_player(self, name, instance):  # pylint: disable=unused-argument
        self.player_db.table.remove(self.player_db.query.name == name)
        self.player_list_update()
