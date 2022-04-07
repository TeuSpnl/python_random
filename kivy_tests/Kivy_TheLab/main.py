from cgitb import text
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutExample(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
        
    #     b1 = Button(text = "Hello")
    #     b2 = Button(text = "B")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()