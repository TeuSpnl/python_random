from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window



class LoginApp(MDApp):
    dialog = None

    def build(self):
        # define theme colors
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Blue"
        # load and return kv string


# run app
LoginApp().run()
