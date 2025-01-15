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
tags = []
removed = []
done = []
todo = []

def bk_addtodo(label,description,time,date,tag):
    compound = [label,description,time,date,tag]
    todo.append(compound)
    if tag != '':
        b1 = 0
        if tags == '':
            b1 += 1
        for object in tags:
            if object[0] == tag:
                b1 += 1
        if b1 == 0:
            tags.append([tag, 'No description yet!'])
    stl = 0
    for oj in todo:
        stl +=1
    print(stl)


def bk_donetodos(id):
    finished = todo.pop(id)
    done.append(finished)
    print(done)

def bk_saveedits(id,label,description,time,date,tag):
    a1 = 0
    for entry in label,description,time,date,tag:
        if entry != '':
            todo[id][a1] = entry
        a1 += 1

    if tag != '':
        b1 = 0
        if tags == '':
            b1 += 1
        for object in tags:
            if object[0] == tag:
                b1 += 1
        if b1 == 0:
            tags.append([tag, 'No description yet!'])


def bk_addtag(label,description):
    compound = [label,description]
    tags.append(compound)

def bk_tagremove(id):
    removed = tags.pop(id)
    done.append(removed)
    print(done)

def bk_savetagedits(id,label,description):
    a1 = 0
    for entry in label,description:
        if entry != '':
            tags[id][a1] = entry
            a1 += 1


#front end-----------------------------------------------------------------------------------------------------------------------------------------
#main grid layout for main todos----------------------------------------------------------------------------------
class MainGridlayout(GridLayout):
    def __init__(self,screen_manager,uppercl, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = dp(10)
        self.spacing = dp(-20)
        self.screen_manager = screen_manager
        self.uppercl = uppercl
        self.refreshmaking()

# a function to remake the whole gridlayout and deletes the finished ones
    def refreshmaking(self):
        self.clear_widgets()
        global todo
        for object in todo:
            self.addnew(object[0],todo.index(object))

#front finising function to pass the selected key and id to the backend
    def fr_tododone(self,instance):
        todo_id = instance.id
        bk_donetodos(todo_id)
        self.refreshmaking()

#the todos editing part
    def preparetoedit(self,instance):
        todo_id = instance.id
        self.uppercl.edittodoresult(todo_id)

    def addnew(self,getting_label,ids):
        self.made_layout = BoxLayout()
        dbtn = Button(text="done", background_color ='darkcyan',background_normal = "", size_hint=(.1, .7))
        dbtn.id = ids
        dbtn.bind(on_press=self.fr_tododone)
        nbtn = (Button(text=f"{getting_label}",font_size='30sp', background_color = 'lightseagreen',background_normal = "", size_hint=(1, .7)))
        nbtn.id = ids
        nbtn.bind(on_press=self.preparetoedit)

        self.made_layout.add_widget(dbtn)
        self.made_layout.add_widget(nbtn)
        self.made_layout.size_x = 1
        self.made_layout.size_hint_y = None
        self.made_layout.size_y = dp(5)
        self.add_widget(self.made_layout)

# main grid layout's scroll feature
class Scrollmain(ScrollView):
    def __init__(self, screen_manager,uppercl, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.72)
        self.pos_hint = {"x": 0, "y": 0.1}
        self.maingrid = MainGridlayout(self,screen_manager, size_hint=(1, None), pos_hint=(0.5, 0.01))
        self.maingrid.bind(minimum_height=self.maingrid.setter('height'))
        self.maingrid.height = self.maingrid.minimum_height
        self.add_widget(self.maingrid)
        self.uppercl = uppercl

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
        self.refresh()

    def refresh(self):
        self.clear_widgets()

        bt1 = Button(text="Tags",size=(dp(200),dp(50)),size_hint=(None,None),font_size='40sp', pos_hint={"right":0.45,"top":0.97},background_color = 'darkcyan',background_normal = ""  )
        bt2 = Button(text="Notes",font_size='40sp',size=(dp(200),dp(50)),size_hint=(None,None), pos_hint={"right":0.82,"top":0.97},background_color = 'darkcyan',background_normal = ""  )
        bt3 = Button(text="Setting",size=(dp(60),dp(30)),size_hint=(None,None),pos_hint={"right":.08,"top":0.99},background_color = 'darkcyan',background_normal = ""  )
        self.add_widget(Button(text="+",font_size='100sp',size=(dp(80),dp(72)),size_hint=(None,None),pos_hint={"right":0.56,"top":0.99}, background_color = 'darkcyan',background_normal = "",on_press=self.maketodoresult))

        def go_sc1(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('first'))
            app.sm.add_widget(Tagscreen(name='first'))
            self.manager.current = 'first'
        def go_sc2(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('second'))
            app.sm.add_widget(Notescreen(name='second'))
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
        self.todo_scroll = Scrollmain(self,self.manager)
        self.add_widget(self.todo_scroll)


    def edittodoresult(self,todo_id):
        self.clear_widgets()
        global todo
        self.add_widget(Button(text="go back", size=(dp(100), dp(50)), size_hint=(None, None),
                               pos_hint={"right": 1, "top": 0.99}, background_color='darkcyan', background_normal="",on_press=self.editback))

        self.labeltx = TextInput(hint_text=f"{todo[todo_id][0]}", halign='center', font_size='20sp',
                                 pos_hint={"right": 0.80, "top": 0.98},
                                 size=(dp(500), dp(40)), size_hint=(None, None), background_color='aquamarine',
                                 background_normal="", multiline=False)
        self.add_widget(self.labeltx)

        self.descriptiontx = TextInput(hint_text=f"{todo[todo_id][1]}", halign='center', font_size='20sp',
                                       pos_hint={"right": 0.64, "top": 0.85},
                                       size=(dp(500), dp(430)), size_hint=(None, None), background_color='aquamarine',
                                       background_normal="", multiline=True)
        self.add_widget(self.descriptiontx)

        self.timetx = TextInput(hint_text=f"{todo[todo_id][2]}", font_size='17sp',
                                pos_hint={"right": 0.95, "top": 0.72}, size=(dp(200), dp(38)),
                                size_hint=(None, None), background_color='turquoise', background_normal="",
                                multiline=False)
        self.add_widget(self.timetx)

        self.datetx = TextInput(hint_text=f"{todo[todo_id][3]}", font_size='17sp',
                                pos_hint={"right": 0.95, "top": 0.80},
                                size=(dp(200), dp(38)), size_hint=(None, None), background_color='turquoise',
                                background_normal="", multiline=False)
        self.add_widget(self.datetx)

        self.add_widget(Label(text="Enter the date and time ", color='aquamarine', font_size='20sp',
                              pos_hint={"right": 0.95, "top": 0.86},
                              size=(dp(200), dp(38)), size_hint=(None, None)))

        self.add_widget(Label(text="Enter the tag/tags", color='aquamarine',
                              font_size='20sp', pos_hint={"right": 0.95, "top": 0.62}, size=(dp(200), dp(38)),
                              size_hint=(None, None)))

        self.tagtx = TextInput(hint_text=f"{todo[todo_id][4]}", font_size='20sp', pos_hint={"right": 0.97, "top": 0.55},
                               size=(dp(250), dp(250)),
                               size_hint=(None, None), background_color='turquoise', background_normal="",
                               multiline=True)
        self.add_widget(self.tagtx)

        self.savepool = Button(text="save", size=(dp(80), dp(40)), size_hint=(None, None),
                               pos_hint={"right": 0.55, "top": 0.1}, background_color='darkcyan', background_normal="",on_press=self.saveback)
        self.savepool.id = todo_id
        self.add_widget(self.savepool)

    def saveback(self,instance):
        todo_id = instance.id
        bk_saveedits(todo_id, self.labeltx.text, self.descriptiontx.text, self.timetx.text, self.datetx.text, self.tagtx.text)
        self.makegridscreen()

    def editback(self,instance):
        self.clear_widgets()
        self.makegridscreen()


    def maketodoresult(self,instance):
        self.clear_widgets()
        self.add_widget(Button(text="go back",on_press=self.exit, size=(dp(100), dp(50)), size_hint=(None, None),
                               pos_hint={"right": 1, "top": 0.99}, background_color='darkcyan', background_normal=""))

        self.labeltx = TextInput(hint_text="Enter the Label", halign='center', font_size='20sp',
                                 pos_hint={"right": 0.80, "top": 0.98},
                                 size=(dp(500), dp(40)), size_hint=(None, None), background_color='aquamarine',
                                 background_normal="", multiline=False)
        self.add_widget(self.labeltx)

        self.descriptiontx = TextInput(hint_text="Enter the description", halign='center', font_size='20sp',
                                       pos_hint={"right": 0.64, "top": 0.85},
                                       size=(dp(500), dp(430)), size_hint=(None, None), background_color='aquamarine',
                                       background_normal="", multiline=True)
        self.add_widget(self.descriptiontx)

        self.timetx = TextInput(hint_text="Time example: 00:00:00", font_size='17sp',
                                pos_hint={"right": 0.95, "top": 0.72}, size=(dp(200), dp(38)),
                                size_hint=(None, None), background_color='turquoise', background_normal="",
                                multiline=False)
        self.add_widget(self.timetx)

        self.datetx = TextInput(hint_text="Date example: 00/00/00", font_size='17sp',
                                pos_hint={"right": 0.95, "top": 0.80},
                                size=(dp(200), dp(38)), size_hint=(None, None), background_color='turquoise',
                                background_normal="", multiline=False)
        self.add_widget(self.datetx)

        self.add_widget(Label(text="Enter the date and time ", color='aquamarine', font_size='20sp',
                              pos_hint={"right": 0.95, "top": 0.86},
                              size=(dp(200), dp(38)), size_hint=(None, None)))

        self.add_widget(Label(text="Enter the tag/tags", color='aquamarine',
                              font_size='20sp', pos_hint={"right": 0.95, "top": 0.62}, size=(dp(200), dp(38)),
                              size_hint=(None, None)))

        self.tagtx = TextInput(hint_text="existing tags : ", font_size='20sp', pos_hint={"right": 0.97, "top": 0.55},
                               size=(dp(250), dp(250)),
                               size_hint=(None, None), background_color='turquoise', background_normal="",
                               multiline=True)
        self.add_widget(self.tagtx)

        self.add_widget(Button(text="save",on_press=self.saveandexit, size=(dp(80), dp(40)), size_hint=(None, None),
                               pos_hint={"right": 0.55, "top": 0.1}, background_color='darkcyan', background_normal=""))

    def exit(self, instance):
        self.makegridscreen()

    def saveandexit(self,instance):
        bk_addtodo(self.labeltx.text, self.descriptiontx.text, self.timetx.text, self.datetx.text, self.tagtx.text)
        self.makegridscreen()

    def makegridscreen(self):
        self.clear_widgets()
        bt1 = Button(text="Tags",size=(dp(200),dp(50)),size_hint=(None,None),font_size='40sp', pos_hint={"right":0.45,"top":0.97},background_color = 'darkcyan',background_normal = ""  )
        bt2 = Button(text="Notes",font_size='40sp',size=(dp(200),dp(50)),size_hint=(None,None), pos_hint={"right":0.82,"top":0.97},background_color = 'darkcyan',background_normal = ""  )
        bt3 = Button(text="Setting",size=(dp(60),dp(30)),size_hint=(None,None),pos_hint={"right":.08,"top":0.99},background_color = 'darkcyan',background_normal = ""  )
        self.add_widget(Button(text="+",font_size='100sp',size=(dp(80),dp(72)),size_hint=(None,None),pos_hint={"right":0.56,"top":0.99}, background_color = 'darkcyan',background_normal = "",on_press=self.maketodoresult))

        def go_sc1(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('first'))
            app.sm.add_widget(Tagscreen(name='first'))
            self.manager.current = 'first'
        def go_sc2(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('second'))
            app.sm.add_widget(Notescreen(name='second'))
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
        self.todo_scroll = Scrollmain(self,self.manager)
        self.add_widget(self.todo_scroll)

# tagscreen--------------------------------------------------------------------------------------------------

class TagGridlayout(GridLayout):
    def __init__(self, screen_manager,uppercl, **kwargs):
        super().__init__(**kwargs)
        self.uppercl = uppercl
        self.cols = 1
        self.padding = dp(10)
        self.spacing = dp(-20)
        self.screen_manager = screen_manager
        self.refreshtagmaking()

    def refreshtagmaking(self):
        self.clear_widgets()
        global tags
        for object in tags:
            self.addnew(object[0],tags.index(object))

    def fr_tagremove(self,instance):
        tag_id = instance.id
        bk_tagremove(tag_id)
        self.refreshtagmaking()

    def preparetoedit(self,instance):
        tag_id = instance.id
        self.uppercl.edittagresult(tag_id)

    def addnew(self,getting_label,ids):
        self.made_layout = BoxLayout()
        tdbtn = Button(text="remove", background_color ='darkcyan',background_normal = "", size_hint=(.1, .7))
        tdbtn.id = ids
        tdbtn.bind(on_press=self.fr_tagremove)
        tnbtn = (Button(text=f"{getting_label}",font_size='30sp', background_color = 'lightseagreen',background_normal = "", size_hint=(1, .7)))
        tnbtn.id = ids
        tnbtn.bind(on_press=self.preparetoedit)

        self.made_layout.add_widget(tdbtn)
        self.made_layout.add_widget(tnbtn)
        self.made_layout.size_x = 1
        self.made_layout.size_hint_y = None
        self.made_layout.size_y = dp(5)
        self.add_widget(self.made_layout)

class Scrolltag(ScrollView):
    def __init__(self, screen_manager,uppercl, **kwargs):
        super().__init__(**kwargs)
        self.uppercl = uppercl
        self.size_hint = (1, 0.72)
        self.pos_hint = {"x": 0, "y": 0.1}
        self.taggrid = TagGridlayout(self,screen_manager, size_hint=(1, None), pos_hint=(0.5, 0.01))
        self.taggrid.bind(minimum_height=self.taggrid.setter('height'))
        self.taggrid.height = self.taggrid.minimum_height
        self.add_widget(self.taggrid)


class Tagscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # apearence
        with self.canvas:
            # screen color managment
            Color(0.280, 0.450, 0.454, 0.700)

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.refresh()

    def refresh(self):
        self.clear_widgets()


        self.add_widget(Button(text="+", font_size='100sp', size=(dp(80), dp(72)), size_hint=(None, None),
                               pos_hint={"right": 0.56, "top": 0.99}, background_color='darkcyan', background_normal="",
                               on_press=self.maketagresult))

        self.add_widget(Button(text="go back", on_press=self.goback, size=(dp(100), dp(50)), size_hint=(None, None),
                               pos_hint={"right": 1, "top": 0.99}, background_color='darkcyan', background_normal=""))

        self.tag_scroll = Scrolltag(self,self.manager)
        self.add_widget(self.tag_scroll)

    def goback(self, instance):
        app = App.get_running_app()
        app.sm.remove_widget(app.sm.get_screen('main'))
        app.sm.add_widget(Mainscreen(name='main'))
        self.manager.current = 'main'


    def edittagresult(self, tag_id):
        self.clear_widgets()
        global tags
        self.add_widget(Button(text="go back", size=(dp(100), dp(50)), size_hint=(None, None),
                                pos_hint={"right": 1, "top": 0.99}, background_color='darkcyan',background_normal="",on_press=self.editback))

        self.labeltx = TextInput(hint_text=f"{tags[tag_id][0]}", halign='center', font_size='20sp',pos_hint={"right": 0.80, "top": 0.98},
                                    size=(dp(500), dp(40)), size_hint=(None, None), background_color='aquamarine',background_normal="", multiline=False)
        self.add_widget(self.labeltx)

        self.descriptiontx = TextInput(hint_text=f"{tags[tag_id][1]}", halign='center', font_size='20sp',pos_hint={"right": 0.64, "top": 0.85},
                                           size=(dp(500), dp(430)), size_hint=(None, None),background_color='aquamarine',
                                           background_normal="", multiline=True)
        self.add_widget(self.descriptiontx)

        self.savepool = Button(text="save", size=(dp(80), dp(40)), size_hint=(None, None),
                                   pos_hint={"right": 0.55, "top": 0.1}, background_color='darkcyan',background_normal="",on_press=self.saveback)
        self.savepool.id = tag_id
        self.add_widget(self.savepool)

    def saveback(self, instance):
        tag_id = instance.id
        bk_savetagedits(tag_id, self.labeltx.text, self.descriptiontx.text)
        self.makegridscreen()

    def editback(self, instance):
        self.clear_widgets()
        self.makegridscreen()


    def maketagresult(self, instance):
        self.clear_widgets()

        self.add_widget(Button(text="go back", on_press=self.exit, size=(dp(100), dp(50)), size_hint=(None, None),
                               pos_hint={"right": 1, "top": 0.99}, background_color='darkcyan', background_normal=""))

        self.labeltx = TextInput(hint_text="Enter the Label", halign='center', font_size='20sp',
                                 pos_hint={"right": 0.55, "top": 0.83},
                                 size=(dp(400), dp(40)), size_hint=(None, None), background_color='aquamarine',
                                 background_normal="", multiline=False)
        self.add_widget(self.labeltx)

        self.descriptiontx = TextInput(hint_text="Enter the description", halign='center', font_size='20sp',
                                       pos_hint={"right": 0.55, "top": 0.75},
                                       size=(dp(400), dp(300)), size_hint=(None, None), background_color='aquamarine',
                                       background_normal="", multiline=True)
        self.add_widget(self.descriptiontx)

        self.add_widget(Button(text="save", on_press=self.saveandexit, size=(dp(80), dp(40)), size_hint=(None, None),
                               pos_hint={"right": 0.55, "top": 0.1}, background_color='darkcyan', background_normal=""))

    def exit(self, instance):
        self.makegridscreen()

    def saveandexit(self, instance):
        bk_addtag(self.labeltx.text, self.descriptiontx.text)
        self.makegridscreen()

    def makegridscreen(self):
        self.clear_widgets()
        self.add_widget(Button(text="+", font_size='100sp', size=(dp(80), dp(72)), size_hint=(None, None),
                               pos_hint={"right": 0.56, "top": 0.99}, background_color='darkcyan', background_normal="",
                               on_press=self.maketagresult))

        self.add_widget(Button(text="go back", on_press=self.goback, size=(dp(100), dp(50)), size_hint=(None, None),
                               pos_hint={"right": 1, "top": 0.99}, background_color='darkcyan', background_normal=""))
        self.tag_scroll = Scrolltag(self,self.manager)
        self.add_widget(self.tag_scroll)

#note screen-----------------------------------------------------------------------------------------------
class Notescreen(Screen):
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

        self.add_widget(Button(text="Todo",font_size='40sp',size=(dp(200),dp(50)),size_hint=(None,None),
                               pos_hint={"right":0.82,"top":0.97},background_color = 'darkcyan',background_normal = ""  ,on_press=self.goback))
        self.add_widget(Button(text="Setting",size=(dp(60),dp(30)),size_hint=(None,None),
                               pos_hint={"right":.08,"top":0.99},background_color = 'darkcyan',background_normal = ""  ))
        self.add_widget(Button(text="Tags",size=(dp(200),dp(50)),size_hint=(None,None),font_size='40sp', pos_hint={"right":0.45,"top":0.97},background_color = 'darkcyan',background_normal = ""  ))
        self.add_widget(Button(text="+",font_size='100sp',size=(dp(80),dp(72)),size_hint=(None,None),
                               pos_hint={"right":0.56,"top":0.99}, background_color = 'darkcyan',background_normal = ""))

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


# main class-------------------------------------------------------------------------------------------------

class Mainapp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Mainscreen(name="main"))
        self.sm.add_widget(Tagscreen(name="first"))
        self.sm.add_widget(Notescreen(name="second"))
        self.sm.add_widget(Settingscreen(name="setting"))
        return self.sm

if __name__ == "__main__":
    Mainapp().run()