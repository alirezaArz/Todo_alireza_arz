from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp

class Mainscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="this is main page"))
        bt1 = Button(text="go to page 1",size=(dp(85),dp(30)),size_hint=(None,None), pos_hint={"x":.40,"y":0.95})
        bt2 = Button(text="go to page 2",size=(dp(85),dp(30)),size_hint=(None,None), pos_hint={"x":.52,"y":0.95})
        def go_sc1(instance):
            self.manager.current = 'first'
        def go_sc2(instance):
            self.manager.current = 'second'
        bt1.bind(on_press=go_sc1)
        bt2.bind(on_press=go_sc2)
        self.add_widget(bt1)
        self.add_widget(bt2)


class First_screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="First Screen"))
        bt1 = Button(text="go back")
        def goback(instance):
            self.manager.current = 'main'
        bt1.bind(on_press=goback)
        self.add_widget(bt1)


class Second_screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Second Screen"))
        bt1 = Button(text="go back")
        def goback(instance):
            self.manager.current = 'main'
        bt1.bind(on_press=goback)
        self.add_widget(bt1)

class Mainapp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Mainscreen(name="main"))
        sm.add_widget(First_screen(name="first"))
        sm.add_widget(Second_screen(name="second"))
        return sm

if __name__ == "__main__":
    Mainapp().run()