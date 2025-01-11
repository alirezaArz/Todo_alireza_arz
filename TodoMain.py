from configobj.validate import bool_dict
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



#back end-------------------------------------------------------------------------------------------------------------------------------------------













#front end-----------------------------------------------------------------------------------------------------------------------------------------

#main grid layout for main todos----------------------------------------------------------------------------------
class MainGridlayout(GridLayout):
    def __init__(self,screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = dp(10)
        self.spacing = dp(-20)
        self.screen_manager = screen_manager


    def addnew(self):
        self.made_layout = BoxLayout()
        self.made_layout.add_widget(Button(text="done", background_color ='darkcyan',background_normal = "", size_hint=(.1, .7)))
        self.made_layout.add_widget(Button(text="todo",on_press=self.go_todoresult, background_color = 'lightseagreen',background_normal = "", size_hint=(1, .7)))
        self.made_layout.size_x = 1
        self.made_layout.size_hint_y = None
        self.made_layout.size_y = dp(5)
        self.add_widget(self.made_layout)

    def go_todoresult(self, instance):
        self.screen_manager.remove_widget(self.screen_manager.get_screen('todoresult'))
        self.screen_manager.add_widget(Todoresultscreen(name='todoresult'))
        self.screen_manager.current = 'todoresult'

# main grid layout's scroll feature
class Scrollmain(ScrollView):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.72)
        self.pos_hint = {"x": 0, "y": 0.1}
        self.maingrid = MainGridlayout(screen_manager, size_hint=(1, None), pos_hint=(0.5, 0.01))
        self.maingrid.bind(minimum_height=self.maingrid.setter('height'))
        self.maingrid.height = self.maingrid.minimum_height
        self.add_widget(self.maingrid)

# main screen
class Mainscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #apearence
        with self.canvas:
            # screen color managment
            Color(0.280,0.450,0.454,0.700)

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

        #the function for making a new page of todo---
        def go_todoresultt(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('todoresult'))
            app.sm.add_widget(Todoresultscreen(name='todoresult'))
            self.manager.current = 'todoresult'


        bt1 = Button(text="Tags",size=(dp(100),dp(40)),size_hint=(None,None), pos_hint={"right":0.98,"top":0.99},background_color = 'darkcyan',background_normal = ""  )
        bt2 = Button(text="Notes",size=(dp(200),dp(50)),size_hint=(None,None), pos_hint={"right":0.82,"top":0.97},background_color = 'darkcyan',background_normal = ""  )
        bt3 = Button(text="Setting",size=(dp(60),dp(30)),size_hint=(None,None),pos_hint={"right":.08,"top":0.99},background_color = 'darkcyan',background_normal = ""  )
        self.add_widget(Label(text="Todo", color='aquamarine',font_size='42sp',bold=True,
                              pos_hint={"right": 0.50, "top": 0.97}, size=(dp(200), dp(50)),size_hint=(None, None)))
        add_todo = Button(text="+",font_size='100sp',size=(dp(74),dp(70)),size_hint=(None,None),pos_hint={"right":0.56,"top":0.99}, background_color = 'darkcyan',background_normal = "",on_press=go_todoresultt  )

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
        self.todo_scroll = Scrollmain(self.manager)
        self.add_widget(self.todo_scroll)
        self.add_widget(add_todo)


# todos result screen--------------------------------------------------------------------------------------
class Todoresultscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # screen color managment
            Color(0.280, 0.450, 0.454, 0.700)

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def goback(self,instance):
        app = App.get_running_app()
        app.sm.remove_widget(app.sm.get_screen('main'))
        app.sm.add_widget(Mainscreen(name='main'))
        self.manager.current = 'main'


    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.add_widget(Button(text="go back",on_press=self.goback, size=(dp(100), dp(50)), size_hint=(None, None),
                               pos_hint={"right": 1, "top": 0.99},background_color='darkcyan', background_normal=""))

        self.add_widget(Button(text="save", on_press=self.goback, size=(dp(80), dp(40)), size_hint=(None, None),
                               pos_hint={"right": 0.55, "top": 0.1}, background_color='darkcyan',background_normal=""))

        self.add_widget(TextInput(hint_text="Enter the Label",halign='center',font_size='20sp',pos_hint={"right": 0.80, "top": 0.98},
                                  size=(dp(500), dp(40)), size_hint=(None, None), background_color='aquamarine',background_normal="",multiline=False))

        self.add_widget(TextInput(hint_text="Enter the description",halign='center', font_size='20sp', pos_hint={"right": 0.64, "top": 0.85},
                                  size=(dp(500), dp(430)), size_hint=(None, None), background_color='aquamarine',background_normal="", multiline=True))
        self.add_widget(
            TextInput(hint_text="Date example: 00/00/00 ", font_size='17sp', pos_hint={"right": 0.95, "top": 0.72},
                      size=(dp(200), dp(38)), size_hint=(None, None), background_color='turquoise',background_normal="", multiline=False))

        self.add_widget(TextInput(hint_text=" Time example: 00:00:00 ", font_size='17sp',
                                  pos_hint={"right": 0.95, "top": 0.80},size=(dp(200), dp(38)), size_hint=(None, None), background_color='turquoise',background_normal="", multiline=False))
        self.add_widget(
            Label(text="Enter the date and time ",color='aquamarine', font_size='20sp', pos_hint={"right": 0.95, "top": 0.86},
                      size=(dp(200), dp(38)), size_hint=(None, None)))
        self.add_widget(Label(text="Enter the tag/tags", color='aquamarine',
                              font_size='20sp',pos_hint={"right": 0.95, "top": 0.62},size=(dp(200), dp(38)), size_hint=(None, None)))

        self.add_widget(TextInput(hint_text="existing tags : ",font_size='20sp',
                                  pos_hint={"right": 0.97, "top": 0.55},size=(dp(250), dp(250)), size_hint=(None, None), background_color='turquoise',background_normal="", multiline=True))


# setting management-----------------------------------------------------------------------------------------
class Settingscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # screen color managment
            Color(0.280, 0.450, 0.454, 0.700)

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        bt1 = Button(text="go back",size=(dp(100),dp(50)),size_hint=(None,None), pos_hint={"right":1,"top":0.99},background_color = (0.235,.522, .486,1),background_normal = "")
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
        with self.canvas:
            # screen color managment
            Color(0.280, 0.450, 0.454, 0.700)

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

        bt1 = Button(text="go back", size_hint=(None, None), size=(dp(100), dp(50)),pos_hint={"right": 1, "top": 0.99},background_color=(0.235, 0.522, 0.486, 1),background_normal="")
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
        with self.canvas:
            # screen color managment
            Color(0.280, 0.450, 0.454, 0.700)

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def goback(self,instance):
        app = App.get_running_app()
        app.sm.remove_widget(app.sm.get_screen('main'))
        app.sm.add_widget(Mainscreen(name='main'))
        self.manager.current = 'main'

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

        self.add_widget(Button(text="Todo", size=(dp(200), dp(50)), size_hint=(None, None),
                     pos_hint={"right": 0.82, "top": 0.97}, background_color='darkcyan', background_normal="",on_press=self.goback))
        self.add_widget(Button(text="Setting", size=(dp(60), dp(30)), size_hint=(None, None),
                     pos_hint={"right": .08, "top": 0.99}, background_color='darkcyan', background_normal=""))
        self.add_widget(Label(text="Notes", color='aquamarine', font_size='42sp', bold=True,
                              pos_hint={"right": 0.50, "top": 0.97}, size=(dp(200), dp(50)), size_hint=(None, None)))
        self.add_widget(Button(text="+", font_size='100sp', size=(dp(74), dp(70)), size_hint=(None, None),
                          pos_hint={"right": 0.56, "top": 0.99}, background_color='darkcyan', background_normal=""))

        self.add_widget(Button(text="go back",size=(dp(100),dp(50)),size_hint=(None,None),
                               pos_hint={"right":1,"top":0.99},background_color = (0.235,.522, .486,1),background_normal = "",on_press=self.goback))


# main class-------------------------------------------------------------------------------------------------

class Mainapp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Mainscreen(name="main"))
        self.sm.add_widget(Tagscreen(name="first"))
        self.sm.add_widget(Second_screen(name="second"))
        self.sm.add_widget(Settingscreen(name="setting"))
        self.sm.add_widget(Todoresultscreen(name="todoresult"))
        return self.sm

if __name__ == "__main__":
    Mainapp().run()