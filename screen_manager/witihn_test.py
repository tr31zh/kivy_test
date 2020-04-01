from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout

Config.set("graphics", "width", "800")
Config.set("graphics", "height", "480")


class RootWidget(BoxLayout):
    pass


class MainWindowManager(ScreenManager):
    pass


class PageOne(Screen):
    page_tile = "Page 1"


class PageTwo(Screen):
    page_tile = "Page 2"


class Footer(BoxLayout):
    current_page = None


class Header(BoxLayout):
    current_page = None


class WithinTestApp(App):
    title = "Within test"

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    rr_app = WithinTestApp()
    rr_app.run()
