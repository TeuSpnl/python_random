from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, BooleanProperty


class ImagesExample(GridLayout, Screen):
    pass


class WidgetsExample(GridLayout, Screen):
    count = 0
    # Specifies the default value of the property to use in the kv file
    enable_count = BooleanProperty(False)
    my_text = StringProperty(str(count))
    slider_text = StringProperty("0")

    def on_button_click(self):
        self.count += 1
        self.my_text = str(self.count)

    def on_toggle_state(self, widget):
        # widget.state shows if the button is normal or down
        if widget.state == "normal":
            widget.text = "OFF"
            self.enable_count = False

        elif widget.state == "down":
            widget.text = "ON"
            self.enable_count = True
    # def on_slider_value(self, widget): # It's raplaced by str(int(slider.value)) in the kv file
    #     format_widget = f"{widget.value:.2f}"
    #     self.slider_text = str(format_widget)


class BoxLayoutExample(BoxLayout, Screen):
    # def __init__(self, **kwargs): #You use it to add graphics throw Python
    #     super().__init__(**kwargs)

    #     b1 = Button(text = "Hello")
    #     b2 = Button(text = "B")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    pass


class ScrollViewEx(ScrollView, Screen):
    pass


class MainWidget(BoxLayout, Screen):
    pass


class TheLabApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainWidget(name='main'))
        sm.add_widget(WidgetsExample(name='widgets'))
        sm.add_widget(BoxLayoutExample(name='box'))
        sm.add_widget(ImagesExample(name='images'))

        return sm


if __name__ == '__main__':
    TheLabApp().run()

# Extra notes:
#
#
#
#
#
#
