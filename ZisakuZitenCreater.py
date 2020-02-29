from kivy.app import App
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.resources import resource_add_path

Builder.load_file("startwindow.kv")
Builder.load_file("mainEditor.kv")

from startWindow import StartWindow
from mainEditor import MainEditor


# font
resource_add_path("fonts/")
LabelBase.register(DEFAULT_FONT, "SourceHanSans.otf")


class MainRoot(BoxLayout):
    startwindow = None
    mainEditor = None

    def __init__(self, **kwargs):
        self.startwindow = Factory.StartWindow()
        self.mainEditor = Factory.MainEditor()
        super(MainRoot, self).__init__(**kwargs)
        self.startwindow_disp()

    def startwindow_disp(self):
        self.clear_widgets()
        self.add_widget(self.startwindow)

    def mainEditor_disp(self):
        self.clear_widgets()
        self.add_widget(self.mainEditor)


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = "hello world"


if __name__ == '__main__':
    MainApp().run()
