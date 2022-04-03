from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder

GUI = Builder.load_file("layout.kv")

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()

if __name__ == '__main__':
    PongApp().run()