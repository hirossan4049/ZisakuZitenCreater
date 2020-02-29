import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# to change the kivy default settings we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)


# class in which we are creating the imagebutton
class ButtonApp(App):

    def build(self):
        # create a fully styled functional button
        # Adding images normal.png and down.png
        btn = Button(text="Push Me !",
                     background_normal='normal.png',
                     background_down='down.png',

                     # Added the border property to round the corners of the button
                     border=(30, 30, 30, 30),

                     size_hint=(.3, .3),
                     pos_hint={"x": 0.35, "y": 0.3}
                     )

        # Returning the button
        return btn

    # creating the object root for ButtonApp() class


if __name__ == '__main__':
    ButtonApp().run()