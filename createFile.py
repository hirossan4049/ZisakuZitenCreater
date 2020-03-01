from kivy.properties import StringProperty, Clock, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from tkinter import filedialog

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class CreateFile(BoxLayout):
    # path = StringProperty()
    def __init__(self, **kwargs):
        super(CreateFile, self).__init__(**kwargs)

    def onClick(self):
        content = SaveDialog()
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()