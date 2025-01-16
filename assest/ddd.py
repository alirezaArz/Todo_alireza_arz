from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput


class MainClass:
    def __init__(self):
        self.middle_instance = MiddleClass(self)

    def main_method(self):
        print("MainClass method called!")


class MiddleClass:
    def __init__(self, parent):
        self.parent = parent  # مرجع به MainClass
        self.button_handler = ButtonClass(self)  # ارسال مرجع به MiddleClass

    def middle_method(self):
        print("MiddleClass method called!")
        self.parent.main_method()  # دسترسی به MainClass


class ButtonClass:
    def __init__(self, parent):
        self.parent = parent  # مرجع به MiddleClass
        button = Button(text="Press me")
        button.bind(on_press=self.call_methods)

    def call_methods(self, instance):
        print("Button pressed!")
        self.parent.middle_method()  # فراخوانی متد در MiddleClass
        self.parent.parent.main_method()  # دسترسی به MainClass از طریق MiddleClass

if __name__ == "__main__":
