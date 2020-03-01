import re

from kivy.properties import StringProperty, Clock, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from tkinter import filedialog

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class SaveDialog(FloatLayout):
    ok_popup = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class CreateFile(FloatLayout):
    # path = StringProperty()
    def __init__(self, **kwargs):
        super(CreateFile, self).__init__(**kwargs)

    def dismiss_popup(self):
        self._popup.dismiss()

    def onClick(self):
        self.createDialog()

    def createDialog(self):
        content = SaveDialog(ok_popup=self.ok_popup, cancel=self.dismiss_popup)
        self._popup = Popup(title="ファイルを作成", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def ok_popup(self, path, filename):
        print(path, filename)
        # if Not Json file
        filenamelist = filename.split(".")
        if not filenamelist[-1] == "json":
            filename = "_".join(filenamelist) + ".json"

        self.ids.pathInput.text = path + "/" + filename
        self.dismiss_popup()
