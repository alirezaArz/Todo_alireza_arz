from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

#main grid layout for main todos
class MainGridlayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = dp(10)
        self.spacing = dp(2)
        # here we define a function to add todos
        def make_new(instance):
            todo=Label(text="done")
            todo.size_x = 1
            todo.size_hint_y = None
            todo.size_y = dp(30)
            self.add_widget(todo)

        add_todo = Button(text="add todo", on_press=make_new)
        add_todo.size_x = 1
        add_todo.size_hint_y = None
        add_todo.size_y = dp(30)
        self.add_widget(add_todo)

# main grid layout's scroll feature
class Scrollmain(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_hint ={"x":0,"y":-.16}
        maingrid = MainGridlayout(size_hint=(1,None), pos_hint=(0.5, 0.01))
        maingrid.bind(minimum_height=maingrid.setter('height'))
        maingrid.height = maingrid.minimum_height
        self.add_widget(maingrid)

# main screen
class Mainscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bt1 = Button(text="Tags",size=(dp(85),dp(30)),size_hint=(None,None), pos_hint={"right":0.5,"top":0.90})
        bt2 = Button(text="not defined",size=(dp(85),dp(30)),size_hint=(None,None), pos_hint={"right":0.62,"top":0.90})
        bt3 = Button(text="setting",size=(dp(85),dp(30)),size_hint=(None,None),pos_hint={"right":0.99,"top":0.99})
        def go_sc1(instance):
            self.manager.current = 'first'
        def go_sc2(instance):
            self.manager.current = 'second'
        def go_sc3(instance):
            self.manager.current = 'setting'

        bt1.bind(on_press=go_sc1)
        bt2.bind(on_press=go_sc2)
        bt3.bind(on_press=go_sc3)
        self.add_widget(bt1)
        self.add_widget(bt2)
        self.add_widget(bt3)

        todo_scroll = Scrollmain(size=(1,1),pos=(.05,0))
        self.add_widget(todo_scroll)

# setting management
class Settingscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        self.add_widget(Label(text="setting"))
        bt1 = Button(text="go back")
        def goback(instance):
            self.manager.current = 'main'
        bt1.bind(on_press=goback)
        self.add_widget(bt1)


# tag screen
class Tagscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="tag screen"))
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
        sm.add_widget(Tagscreen(name="first"))
        sm.add_widget(Second_screen(name="second"))
        sm.add_widget(Settingscreen(name="setting"))
        return sm

if __name__ == "__main__":
    Mainapp().run()