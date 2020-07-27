#!/usr/bin/env python3

import kivy
from os import system
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
Window.size = (500, 500)

class Installer(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        EOPKG = Button(text="eopkg")
        EOPKG.bind(on_press=self.buttonEOPKG)
        SNAPD = Button(text="snapd")
        SNAPD.bind(on_press=self.buttonSNAPD)
        self.label = Label(text="Install with:")
        layout.add_widget(self.label)
        layout.add_widget(EOPKG)
        layout.add_widget(SNAPD)
        self.text = TextInput(text='', multiline=False)
        layout.add_widget(self.text)
        return layout
    
    def buttonEOPKG(self, EOPKG):
        self.label.text = "Installing " + self.text.text
        system("sudo eopkg install " + self.text.text)
        print("Done!")
    
    def buttonSNAPD(self, SNAPD):
        self.label.text = "Installing " + self.text.text
        system("sudo snap install " + self.text.text)
        print("Done!")

if __name__ == "__main__":
    Installer().run()