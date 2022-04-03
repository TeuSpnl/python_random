from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

from kivy.properties import ObjectProperty

from kivy.lang import Builder

GUI = Builder.load_file("layout.kv")

class CustomLayout(GridLayout):
    background_image = ObjectProperty(
        Image(
            source = './goku_sunset.gif',
            anim_delay = .1))

class RootWidget(FloatLayout):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()