from docutils.utils import release_level_abbreviations
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

#main grid layout for main todos----------------------------------------------------------------------------------
class MainGridlayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = dp(10)
        self.spacing = dp(-20)
    def addnew(self):
        made_layout = BoxLayout()
        made_layout.add_widget(Button(text="done", background_color ='darkcyan',background_normal = "", size_hint=(.1, .7)))
        made_layout.add_widget(Button(text="todo", background_color = 'lightseagreen',background_normal = "", size_hint=(1, .7)))
        made_layout.size_x = 1
        made_layout.size_hint_y = None
        made_layout.size_y = dp(5)
        self.add_widget(made_layout)

# main grid layout's scroll feature
class Scrollmain(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1,0.72)
        self.pos_hint ={"x":0,"y":0.1}
        self.maingrid = MainGridlayout(size_hint=(1,None), pos_hint=(0.5, 0.01))
        self.maingrid.bind(minimum_height=self.maingrid.setter('height'))
        self.maingrid.height = self.maingrid.minimum_height
        self.add_widget(self.maingrid)

# main screen
class Mainscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            # screen color managment
            Color(0.280,0.450,0.454,0.700)

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

        def addnumber(instance):
            self.todo_scroll.maingrid.addnew()

        bt1 = Button(text="Tags",size=(dp(100),dp(40)),size_hint=(None,None), pos_hint={"right":0.72,"top":0.99},background_color = 'darkcyan',background_normal = ""  )
        bt2 = Button(text="not defined",size=(dp(100),dp(40)),size_hint=(None,None), pos_hint={"right":0.85,"top":0.99},background_color = 'darkcyan',background_normal = ""  )
        bt3 = Button(text="setting",size=(dp(100),dp(40)),size_hint=(None,None),pos_hint={"right":0.98,"top":0.99},background_color = 'darkcyan',background_normal = ""  )
        add_todo = Button(text="+",font_size='100sp',size=(dp(74),dp(70)),size_hint=(None,None),pos_hint={"right":0.98,"top":0.90}, background_color = 'darkcyan',background_normal = "",on_press=addnumber  )
        def go_sc1(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('first'))
            app.sm.add_widget(Tagscreen(name='first'))
            self.manager.current = 'first'
        def go_sc2(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('second'))
            app.sm.add_widget(Second_screen(name='second'))
            self.manager.current = 'second'
        def go_sc3(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('setting'))
            app.sm.add_widget(Settingscreen(name='setting'))
            self.manager.current = 'setting'
        bt1.bind(on_press=go_sc1)
        bt2.bind(on_press=go_sc2)
        bt3.bind(on_press=go_sc3)
        self.add_widget(bt1)
        self.add_widget(bt2)
        self.add_widget(bt3)
        self.todo_scroll = Scrollmain()
        self.add_widget(self.todo_scroll)
        self.add_widget(add_todo)


# setting management-----------------------------------------------------------------------------------------
class Settingscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        self.add_widget(Label(text="setting"))
        bt1 = Button(text="go back",size=(dp(100),dp(50)),size_hint=(None,None), pos_hint={"right":1,"top":1},background_color = (0.235,.522, .486,1),background_normal = "")
        def goback(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('main'))
            app.sm.add_widget(Mainscreen(name='main'))
            self.manager.current = 'main'
        bt1.bind(on_press=goback)
        self.add_widget(bt1)

# tagscreen--------------------------------------------------------------------------------------------------
class Tagscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bt1 = Button(text="go back", size_hint=(None, None), size=(dp(100), dp(50)),
                     pos_hint={"right": 1, "top": 1},
                     background_color=(0.235, 0.522, 0.486, 1),
                     background_normal="")
        def goback(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('main'))
            app.sm.add_widget(Mainscreen(name='main'))
            self.manager.current = 'main'
        bt1.bind(on_press=goback)
        self.add_widget(bt1)
        tagscroll = Tagsscroll()
        self.add_widget(tagscroll)

class Tagsscroll(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.9)
        self.pos_hint = {"center_x": 0.5, "y": 0.0}
        taggrid = Taggrid(size_hint=(1, None))
        taggrid.bind(minimum_height=taggrid.setter('height'))
        taggrid.height = taggrid.minimum_height
        self.add_widget(taggrid)

class Taggrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = dp(10)
        self.spacing = dp(1)

        made_layout = BoxLayout()
        made_layout.add_widget(Button(text="Tag", size_hint=(1, .8)))
        made_layout.size_x = 1
        made_layout.size_hint_y = None
        made_layout.size_y = dp(.5)
        self.add_widget(made_layout)

#second screen-----------------------------------------------------------------------------------------------
class Second_screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Second Screen"))
        bt1 = Button(text="go back",size=(dp(100),dp(50)),size_hint=(None,None), pos_hint={"right":1,"top":1},background_color = (0.235,.522, .486,1),background_normal = "")
        def goback(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('main'))
            app.sm.add_widget(Mainscreen(name='main'))
            self.manager.current = 'main'
        bt1.bind(on_press=goback)
        self.add_widget(bt1)

class Mainapp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Mainscreen(name="main"))
        self.sm.add_widget(Tagscreen(name="first"))
        self.sm.add_widget(Second_screen(name="second"))
        self.sm.add_widget(Settingscreen(name="setting"))
        return self.sm

if __name__ == "__main__":
    Mainapp().run()