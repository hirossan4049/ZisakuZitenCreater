from kivy.app import App
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.resources import resource_add_path

Builder.load_file("startwindow.kv")
Builder.load_file("mainEditor.kv")
Builder.load_file("createFile.kv")

# FIXME:一度にすべてのclassを呼ぶのはいかがなものか。
from startWindow import StartWindow
from mainEditor import MainEditor
from createFile import CreateFile

# font
resource_add_path("fonts/")
LabelBase.register(DEFAULT_FONT, "SourceHanSans.otf")


class MainRoot(BoxLayout):
    startwindow = None
    createFile = None
    mainEditor = None

    # path = StringProperty()
    def __init__(self, **kwargs):
        self.startwindow = Factory.StartWindow()
        self.mainEditor = Factory.MainEditor()
        self.createFile = Factory.CreateFile()
        # self.path = "hello "
        super(MainRoot, self).__init__(**kwargs)
        self.startwindow_disp()

    def startwindow_disp(self):
        self.clear_widgets()
        self.add_widget(self.startwindow)

    def createFile_disp(self):
        self.clear_widgets()
        # self.createFile.path = "hello"
        self.add_widget(self.createFile)

    def maineditor_disp(self, path):
        self.clear_widgets()
        self.add_widget(self.mainEditor)


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = "自作辞典Creator"


if __name__ == '__main__':
    MainApp().run()
