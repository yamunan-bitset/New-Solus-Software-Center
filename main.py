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


class Display(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        self.lbl1 = Label(text="test")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False)
        layout.add_widget(self.txt1)
        return layout

    def buttonClicked(self,btn):
        self.lbl1.text = "Searched Results for " + self.txt1.text
        print("eopkg\n\n")
        system("eopkg search " + self.txt1.text)
        print("\n\nsnapd\n\n")
        system("snap search " + self.txt1.text)
        print("\n\n")


if __name__ == "__main__":
    Display().run()