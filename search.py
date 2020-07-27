#!/usr/bin/env python3

from os import system
from kivy.core.window import Window
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
Window.size = (500, 500)

class Search(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        button = Button(text="OK")
        button.bind(on_press=self.buttonClicked)
        layout.add_widget(button)
        self.label = Label(text="Search")
        layout.add_widget(self.label)
        self.text = TextInput(text='', multiline=False)
        layout.add_widget(self.text)
        return layout

    def buttonClicked(self, button):
        self.label.text = "Searched Results for " + self.text.text
        system("gnome-terminal --command=\'bash -c \"echo \"eopkg\" && eopkg search " + self.text.text + " && echo \"snapd\" && snap search " + self.text.text + ";$SHELL\"\'")

try:

    if __name__ == "__main__":
        Search().run()

except FileNotFoundError:
    Search().run()

