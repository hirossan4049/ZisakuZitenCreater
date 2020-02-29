from kivy.uix.boxlayout import BoxLayout


class StartWindow(BoxLayout):
    print("startWindow.py")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def btn_press(self):
        print("btn press")