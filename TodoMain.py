from itertools import combinations
from kivy.config import Config
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
from kivy.uix.pagelayout import PageLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
import pickle
from kivy.config import Config


#back end-------------------------------------------------------------------------------------------------------------------------------------------

tags = []
removed = []
done = []
todo = []

#color containers-----------------

button_save = [(0.2039, 0.2275, 0.2500, 1)
,(0.4235, 0.4588, 0.4902, 1),(0.4667, 0.8941, 0.7843, 1),
(0.5765, 0.3686, 0.2196, 1),(1.0, 0.1216, 0.5608, 1)
]
back_save = [(0.4235, 0.4588, 0.4902, 1)
,(0.4235, 0.4588, 0.4902, 1),(0.0078, 0.7647, 0.6039, 1)
,(0.4353, 0.3216, 0.2314, 1),(0.6667, 0.0667, 0.3333, 1)]

remove_save = [(0.1294, 0.1451, 0.1608, 1)
,'salmon','salmon',(0.8392, 0.1569, 0.1569, 1)
,'salmon']
recover_save = [(0.6784, 0.7098, 0.7412, 1)
,'lightblue',(0.7176, 0.8941, 0.7804, 1),(0.7176, 0.4118, 0.2078, 1)
,(1.0, 0.9333, 0.5333, 1)
]

ground_save = [(0.9725, 0.9765, 0.9804, 1),(0.2039, 0.2275, 0.2500, 1),
    (0.0, 0.5451, 0.5451, 0.458),
    (0.1490, 0.2353, 0.2549, 1),(0.2980, 0.0235, 0.1137, 1)]

hint_text_save = ['white','white','white','white','white']
foreground_color_save = ['white','white','white','white','white']
done_color_save = ['salmon','salmon','salmon','salmon','salmon']

cl_donecolor = ['black']
cl_ground = [0.2039, 0.2275, 0.2500, 1]
cl_button = [(0.4235, 0.4588, 0.4902, 1)]
cl_back = [(0.4235, 0.4588, 0.4902, 1)]
cl_recover = ['lightblue']
cl_remove = ['tomato']
cl_hintcolor = ['white']
cl_foregroundcolor = ['oldlace']

#main bk functions--------------------------

def saveimport():
    try:
        with open('savedDt.pdt', 'rb') as file:
            newdata = pickle.load(file)
            todo[:] = newdata[0]
            tags[:] = newdata[1]
            removed[:] = newdata[2]
            done[:] = newdata[3]
            print(newdata[6])
            cl_button[:] = newdata[4]
            cl_back[:] = newdata[5]
            cl_ground[:] = newdata[6][:]
            cl_recover[:] = newdata[7]
            cl_donecolor[:] = newdata[8]
            cl_remove[:] = newdata[9]
    except (IndexError, FileNotFoundError):
        pass

combinated = [todo, tags, removed, done, cl_button, cl_back, cl_ground, cl_recover, cl_donecolor, cl_remove]
def savedexport():
    try:
        with open('savedDt.pdt', 'wb') as file:
            pickle.dump(combinated, file)
    except (IndexError, FileNotFoundError):
        pass


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
    savedexport()
    stl = 0
    for oj in todo:
        stl +=1

def bk_donetodos(id):
    finished = todo.pop(id)
    done.append(finished)
    savedexport()


def bk_saveedits(protocol,id,label,description,time,date,tag):
    a1 = 0
    for entry in label,description,time,date,tag:
        src = ''
        if protocol == '1':
            src = todo
        elif protocol == '2':
            src = done

        if entry != '':
            src[id][a1] = entry
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
    savedexport()


def bk_addtag(label,description):
    compound = [label,description]
    tags.append(compound)
    savedexport()

def bk_savetagedits(id,label,description):
    if label != '':
        tags[id][0] = label
    tags[id][1] = description

    savedexport()

#color strategy---------------------------------------------------------

def theme(theme_id):
    cl_button[0] = button_save[theme_id]
    cl_back[0] = back_save[theme_id]
    cl_hintcolor[0] = hint_text_save[theme_id]
    cl_foregroundcolor[0] = foreground_color_save[theme_id]
    cl_donecolor[0] = done_color_save[theme_id]
    cl_ground[:] = ground_save[theme_id]
    cl_recover[0] = recover_save[theme_id]
    cl_remove[0] = remove_save[theme_id]

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
        global done
        for object in todo:
            self.addnew(object[0],todo.index(object))
        for object in done:
            self.donenew(object[0],done.index(object))

#front finising function to pass the selected key and id to the backend
    def fr_tododone(self,instance):
        todo_id = instance.id
        bk_donetodos(todo_id)
        self.refreshmaking()

    def fr_remove(self,instance):
        global done
        done_id = instance.id
        done.pop(done_id)
        savedexport()
        self.refreshmaking()

    def fr_recover(self,instance):
        global done
        done_id = instance.id
        object = done.pop(done_id)
        todo.append(object)
        savedexport()
        self.refreshmaking()
#the todos editing part
    def preparetoedit(self,instance):
        todo_id = instance.id
        protocol = instance.protocol
        self.uppercl.edittodoresult(todo_id,protocol)

    def addnew(self,getting_label,ids):
        self.made_layout = BoxLayout()
        dbtn = Button(size=(dp(80),dp(80)),size_hint=(None,None),background_normal='assest/icons/check/icon.png',background_down='assest/icons/check/icon.png',background_color=cl_button[0])
        dbtn.id = ids
        dbtn.bind(on_press=self.fr_tododone)
        nbtn = (Button(text=f"{getting_label}",background_normal="",font_size='30sp', background_color = cl_back[0], size_hint=(1, .7)))
        nbtn.id = ids
        nbtn.protocol = '1'
        nbtn.bind(on_press=self.preparetoedit)

        self.made_layout.add_widget(dbtn)
        self.made_layout.add_widget(nbtn)
        self.made_layout.size_x = 1
        self.made_layout.size_hint_y = None
        self.made_layout.size_y = dp(5)
        self.add_widget(self.made_layout)

    def donenew(self, getting_label, ids):
        self.made_layout = BoxLayout()

        dbtn = Button(background_normal='assest/icons/recover/icon.png',
                     background_down='assest/icons/recover/icon.png',background_color=cl_recover[0],size=(dp(80),dp(80)),size_hint=(None,None),
                      on_press=self.fr_recover)
        dbtn.id = ids

        xbtn = Button(background_normal='assest/icons/remove/icon.png',
                     background_down='assest/icons/remove/icon.png',background_color=cl_remove[0],size=(dp(80),dp(80)),size_hint=(None,None),
                      on_press=self.fr_remove)
        xbtn.id = ids

        nbtn = (Button(text=f"{getting_label}", font_size='30sp', background_color=cl_donecolor[0],
                   background_normal="",size_hint=(1, .7),on_press=self.preparetoedit))
        nbtn.protocol = '2'
        nbtn.id = ids

        self.made_layout.add_widget(dbtn)
        self.made_layout.add_widget(xbtn)
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
        saveimport()
        with self.canvas:
            global cl_ground
            # screen color managment
            Color(cl_ground[0],cl_ground[1],cl_ground[2],cl_ground[3])

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        saveimport()
        self.refresh()
        #-------------------------------------------------------------------------start coloring
    def refresh(self):
        self.clear_widgets()
        global cl_button
        Config.set('graphics', 'resizable', True)
        bt1 = Button(background_normal='assest/icons/tag/icon.png',
                     background_down='assest/icons/tag/icon.png',background_color=cl_button[0],size=(dp(60),dp(60)),size_hint=(None,None),
                     pos_hint={"right": 0.88,"top": 1})

        bt3 = Button(background_normal='assest/icons/setting/icon.png',
                     background_down='assest/icons/setting/icon.png',background_color=cl_button[0],size=(dp(60),dp(60)),size_hint=(None,None),
                     pos_hint={"right": 0.09, "top": 0.98})

        self.add_widget(Button(background_normal='assest/icons/add/icon.png',
                               background_down='assest/icons/add/icon.png',background_color=cl_button[0],size=(dp(100), dp(100)),
                               size_hint=(None, None),
                               pos_hint={"right": 1, "top": 1},
                               on_press=self.maketodoresult))

        def go_sc1(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('first'))
            app.sm.add_widget(Tagscreen(name='first'))
            self.manager.current = 'first'
        def go_sc3(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('setting'))
            app.sm.add_widget(Settingscreen(name='setting'))
            self.manager.current = 'setting'
        bt1.bind(on_press=go_sc1)
        bt3.bind(on_press=go_sc3)
        self.add_widget(bt1)
        self.add_widget(bt3)
        self.todo_scroll = Scrollmain(self,self.manager)
        self.add_widget(self.todo_scroll)


    def edittodoresult(self,todo_id,protocol):
        self.clear_widgets()
        global done
        global todo
        if protocol == '1':
            src = todo
        elif protocol == '2':
            src = done
        self.add_widget(Button(background_normal='assest/icons/back/icon.png',
                               background_down='assest/icons/back/icon.png',size=(dp(80),dp(80)),size_hint=(None,None),
                               pos_hint={"right": 1, "top": 1},background_color=cl_button[0],on_press=self.editback))

        self.labeltx = TextInput(hint_text=f"{src[todo_id][0]}",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], halign='center', font_size='20sp',
                                 pos_hint={"right": 0.80, "top": 0.98},
                                 size=(dp(500), dp(40)), size_hint=(None, None), background_color=cl_back[0],
                                 multiline=False)
        self.add_widget(self.labeltx)

        self.descriptiontx = TextInput(hint_text=f"{src[todo_id][1]}",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], halign='center', font_size='20sp',
                                       pos_hint={"right": 0.64, "top": 0.85},
                                       size=(dp(500), dp(430)), size_hint=(None, None), background_color=cl_back[0],
                                       multiline=True)
        self.add_widget(self.descriptiontx)

        self.timetx = TextInput(hint_text=f"{src[todo_id][2]}",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], font_size='17sp',
                                pos_hint={"right": 0.95, "top": 0.72}, size=(dp(200), dp(38)),
                                size_hint=(None, None), background_color=cl_back[0],
                                multiline=False)
        self.add_widget(self.timetx)

        self.datetx = TextInput(hint_text=f"{src[todo_id][3]}",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], font_size='17sp',
                                pos_hint={"right": 0.95, "top": 0.80},
                                size=(dp(200), dp(38)), size_hint=(None, None), background_color=cl_back[0],
                                multiline=False)
        self.add_widget(self.datetx)

        self.add_widget(Label(text="Enter the date and time ", color=cl_back[0], font_size='20sp',
                              pos_hint={"right": 0.95, "top": 0.86},
                              size=(dp(200), dp(38)), size_hint=(None, None)))

        self.add_widget(Label(text="Enter the tag/tags", color=cl_back[0],
                              font_size='20sp', pos_hint={"right": 0.95, "top": 0.62}, size=(dp(200), dp(38)),
                              size_hint=(None, None)))

        self.tagtx = TextInput(hint_text=f"{src[todo_id][4]}",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], font_size='20sp', pos_hint={"right": 0.97, "top": 0.55},
                               size=(dp(250), dp(250)),
                               size_hint=(None, None), background_color=cl_back[0],
                               multiline=True)
        self.add_widget(self.tagtx)

        self.savepool = Button(background_normal='assest/icons/save/icon.png',
                               background_down='assest/icons/save/icon.png',size=(dp(60),dp(60)),background_color=cl_button[0],size_hint=(None,None),
                               pos_hint={"right": 0.55, "top": 0.12},on_press=self.saveback)
        self.savepool.protocol = protocol
        self.savepool.id = todo_id
        self.add_widget(self.savepool)

    def saveback(self,instance):
        protocol = instance.protocol
        todo_id = instance.id
        bk_saveedits(protocol, todo_id, self.labeltx.text, self.descriptiontx.text, self.timetx.text, self.datetx.text, self.tagtx.text)
        self.makegridscreen()

    def editback(self,instance):
        self.clear_widgets()
        self.makegridscreen()


    def maketodoresult(self,instance):
        self.clear_widgets()
        self.add_widget(Button(background_normal='assest/icons/back/icon.png',
                               background_down='assest/icons/back/icon.png',size=(dp(80),dp(80)),size_hint=(None,None),
                               pos_hint={"right": 1, "top": 1},background_color=cl_button[0],on_press=self.exit))

        self.labeltx = TextInput(hint_text="Enter the Label",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], halign='center', font_size='20sp',
                                 pos_hint={"right": 0.80, "top": 0.98},
                                 size=(dp(500), dp(40)), size_hint=(None, None), background_color=cl_back[0],
                                 multiline=False)
        self.add_widget(self.labeltx)

        self.descriptiontx = TextInput(hint_text="Enter the description",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], halign='center', font_size='20sp',
                                       pos_hint={"right": 0.64, "top": 0.85},
                                       size=(dp(500), dp(430)), size_hint=(None, None), background_color=cl_back[0],
                                       multiline=True)
        self.add_widget(self.descriptiontx)

        self.timetx = TextInput(hint_text="Time example: 00:00:00",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], font_size='17sp',
                                pos_hint={"right": 0.95, "top": 0.72}, size=(dp(200), dp(38)),
                                size_hint=(None, None), background_color=cl_back[0],
                                multiline=False)
        self.add_widget(self.timetx)

        self.datetx = TextInput(hint_text="Date example: 00/00/00",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], font_size='17sp',
                                pos_hint={"right": 0.95, "top": 0.80},
                                size=(dp(200), dp(38)), size_hint=(None, None), background_color=cl_back[0],
                                multiline=False)
        self.add_widget(self.datetx)

        self.add_widget(Label(text="Enter the date and time ", color=cl_back[0], font_size='20sp',
                              pos_hint={"right": 0.95, "top": 0.86},
                              size=(dp(200), dp(38)), size_hint=(None, None)))

        self.add_widget(Label(text="Enter the tag/tags", color=cl_back[0],
                              font_size='20sp', pos_hint={"right": 0.95, "top": 0.62}, size=(dp(200), dp(38)),
                              size_hint=(None, None)))

        self.tagtx = TextInput(hint_text="existing tags : ",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0], font_size='20sp', pos_hint={"right": 0.97, "top": 0.55},
                               size=(dp(250), dp(250)),
                               size_hint=(None, None), background_color=cl_back[0],
                               multiline=True)
        self.add_widget(self.tagtx)

        self.add_widget(Button(background_normal='assest/icons/save/icon.png',
                               background_down='assest/icons/save/icon.png',size=(dp(60),dp(60)),size_hint=(None,None),
                               pos_hint={"right": 0.55, "top": 0.12},background_color=cl_button[0],on_press=self.saveandexit))

    def exit(self, instance):
        self.makegridscreen()

    def saveandexit(self,instance):
        bk_addtodo(self.labeltx.text, self.descriptiontx.text, self.timetx.text, self.datetx.text, self.tagtx.text)
        self.makegridscreen()

    def makegridscreen(self):
        self.clear_widgets()
        global cl_button
        Config.set('graphics', 'resizable', True)
        bt1 = Button(background_normal='assest/icons/tag/icon.png',
                     background_down='assest/icons/tag/icon.png', size=(dp(60), dp(60)),background_color=cl_button[0], size_hint=(None, None),
                     pos_hint={"right": 0.88,"top": 1})

        bt3 = Button(background_normal='assest/icons/setting/icon.png',background_color=cl_back[0],
                     background_down='assest/icons/setting/icon.png', size=(dp(60), dp(60)),
                     size_hint=(None, None),
                     pos_hint={"right": 0.09, "top": 0.98})

        self.add_widget(Button(background_normal='assest/icons/add/icon.png',
                               background_down='assest/icons/add/icon.png',background_color=cl_button[0], size=(dp(100), dp(100)),
                               size_hint=(None, None),
                               pos_hint={"right": 1, "top": 1},
                               on_press=self.maketodoresult))

        def go_sc1(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('first'))
            app.sm.add_widget(Tagscreen(name='first'))
            self.manager.current = 'first'

        def go_sc3(instance):
            app = App.get_running_app()
            app.sm.remove_widget(app.sm.get_screen('setting'))
            app.sm.add_widget(Settingscreen(name='setting'))
            self.manager.current = 'setting'
        bt1.bind(on_press=go_sc1)
        bt3.bind(on_press=go_sc3)
        self.add_widget(bt1)
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
        global tags
        tag_id = instance.id
        tags.pop(tag_id)
        savedexport()
        self.refreshtagmaking()

    def preparetoedit(self,instance):
        tag_id = instance.id
        self.uppercl.edittagresult(tag_id)

    def addnew(self,getting_label,ids):
        self.made_layout = BoxLayout()
        tdbtn = Button(size=(dp(80),dp(80)),size_hint=(None,None),background_normal='assest/icons/remove/icon.png',
                       background_down='assest/icons/remove/icon.png',background_color=cl_back[0])
        tdbtn.id = ids
        tdbtn.bind(on_press=self.fr_tagremove)
        tnbtn = (Button(text=f"{getting_label}",font_size='30sp',background_normal="",
                        background_color = cl_back[0], size_hint=(1, .7)))
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
            Color(cl_ground[0],cl_ground[1],cl_ground[2],cl_ground[3])

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.refresh()

    def refresh(self):
        self.clear_widgets()

        self.add_widget(Button(background_normal='assest/icons/tag_add/icon.png',
            background_down='assest/icons/tag_add/icon.png', size=(dp(80), dp(80)),
            size_hint=(None, None),pos_hint={"right": 0.90, "top": 1},background_color=cl_button[0],on_press=self.maketagresult))

        self.add_widget(Button(background_normal='assest/icons/back/icon.png',
                               background_down='assest/icons/back/icon.png', size=(dp(80), dp(80)),
                               size_hint=(None, None),
                               pos_hint={"right": 1, "top": 1},background_color=cl_button[0],on_press=self.goback))

        self.tag_scroll = Scrolltag(self,self.manager)
        self.add_widget(self.tag_scroll)

    def goback(self, instance):
        app = App.get_running_app()
        app.sm.remove_widget(app.sm.get_screen('main'))
        app.sm.add_widget(Mainscreen(name='main'))
        self.manager.current = 'main'


    def edittagresult(self, tag_id):
        self.clear_widgets()
        global todo
        todoamount = 0
        for objects in todo:
            if tags[tag_id][0] == objects[4]:
                todoamount += 1
        if todoamount == 0:
            jm = f'There are no todos\ncurrently using this tag'
        elif todoamount == 1:
            jm = f'There is one todo\ncurrently using this tag'
        else:
            jm = f'there are {todoamount}\ntodos currently using this tag'


        self.add_widget(Label(text=jm,color=cl_back, font_size='25sp',
                        pos_hint={"right": 0.62, "top": 0.25},bold=True,
                        size=(dp(200), dp(38)), size_hint=(None, None)))

        self.add_widget(Button(background_normal='assest/icons/back/icon.png',
                               background_down='assest/icons/back/icon.png', size=(dp(80), dp(80)),
                               size_hint=(None, None),
                               pos_hint={"right": 1, "top": 1},background_color=cl_button[0],on_press = self.editback))

        self.labeltx = TextInput(hint_text=f"{tags[tag_id][0]}",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0],
                                 halign='center', font_size='20sp',pos_hint={"right": 0.73, "top": 0.88},
                                 size=(dp(400), dp(40)), size_hint=(None, None), background_color=cl_back, multiline=False)
        self.add_widget(self.labeltx)

        self.descriptiontx = TextInput(hint_text=f"{tags[tag_id][1]}",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0],
                                       halign='center', font_size='20sp',pos_hint={"right": 0.73, "top": 0.80},
                                       size=(dp(400), dp(300)), size_hint=(None, None), background_color=cl_back[0], multiline=True)
        self.add_widget(self.descriptiontx)

        self.savepool = Button(background_normal='assest/icons/save/icon.png',
                               background_down='assest/icons/save/icon.png', size=(dp(60), dp(60)),
                               size_hint=(None, None),
                               pos_hint={"right": 0.55, "top": 0.12},background_color=cl_button[0], on_press=self.saveback)

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

        self.add_widget(Button(background_normal='assest/icons/back/icon.png',
                               background_down='assest/icons/back/icon.png', size=(dp(80), dp(80)),
                               size_hint=(None, None), pos_hint={"right": 1, "top": 1},background_color=cl_button[0],on_press=self.exit))

        self.labeltx = TextInput(hint_text="Enter the Label",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0],
                                 halign='center', font_size='20sp',pos_hint={"right": 0.73, "top": 0.88},
                                 size=(dp(400), dp(40)), size_hint=(None, None), background_color=cl_back[0], multiline=False)
        self.add_widget(self.labeltx)

        self.descriptiontx = TextInput(hint_text="Enter the description",hint_text_color=cl_hintcolor[0],foreground_color=cl_foregroundcolor[0],
                                       halign='center', font_size='20sp',pos_hint={"right": 0.73, "top": 0.80},
                                       size=(dp(400), dp(300)), size_hint=(None, None), background_color=cl_back[0], multiline=True)
        self.add_widget(self.descriptiontx)

        self.add_widget(Button(background_normal='assest/icons/save/icon.png',
                               background_down='assest/icons/save/icon.png', size=(dp(60), dp(60)),
                               size_hint=(None, None),
                               pos_hint={"right": 0.55, "top": 0.12},background_color=cl_button[0], on_press=self.saveandexit))

    def exit(self, instance):
        self.makegridscreen()

    def saveandexit(self, instance):
        bk_addtag(self.labeltx.text, self.descriptiontx.text)
        self.makegridscreen()

    def makegridscreen(self):
        self.clear_widgets()
        self.add_widget(Button(background_normal='assest/icons/tag_add/icon.png',
                               background_down='assest/icons/tag_add/icon.png', size=(dp(80), dp(80)),
                               size_hint=(None, None), pos_hint={"right": 0.90, "top": 1},background_color=cl_button[0],on_press=self.maketagresult))

        self.add_widget(Button(background_normal='assest/icons/back/icon.png',
                               background_down='assest/icons/back/icon.png',background_color=cl_button[0], size=(dp(80), dp(80)),
                               size_hint=(None, None),
                               pos_hint={"right": 1, "top": 1}, on_press=self.goback))
        self.tag_scroll = Scrolltag(self,self.manager)
        self.add_widget(self.tag_scroll)

# setting management-----------------------------------------------------------------------------------------
class Settingscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # screen color managment
            Color(cl_ground[0],cl_ground[1],cl_ground[2],cl_ground[3])

            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        self.clear_widgets()
        self.makesettings()
    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos



    def makesettings(self):
        self.add_widget(Button(background_normal='assest/icons/back/icon.png',
                           background_down='assest/icons/back/icon.png', size=(dp(80), dp(80)),
                           size_hint=(None, None),
                           pos_hint={"right": 1, "top": 1},on_press=self.goback,background_color=cl_button[0]))
        # apearance setting---------------------
        self.aprence = BoxLayout()
        self.aprence.orientation = 'horizontal'
        self.aprence.size_hint_x = 0.6
        self.aprence.size_hint_y = .1
        self.aprence.pos_hint= {'right':0.62, 'top': 0.90}
        self.add_widget(self.aprence)

        self.add_widget(Label(text="appearance",color=cl_back[0],
                              font_size='30sp', pos_hint={"right": 0.25, "top": 0.98}, size=(dp(200), dp(38)),
                              size_hint=(None, None)))

        ap1 = ToggleButton(text='Light',on_press=self.fr_theme,color='white',background_color='white',font_size='30sp',bold=True, group='apprence', size=(0.2,1),
                         pos_hint={"right": 1, "top": .90})
        ap1.id = 0

        ap2 = ToggleButton(text='Dark',on_press=self.fr_theme,color='gray',background_color='black',font_size='30sp',bold=True, group='apprence', size=(0.2,1),
                         pos_hint={"right": 1, "top": .90})
        ap2.id = 1

        ap3 = ToggleButton(text='Forest',on_press=self.fr_theme,color='lightblue',background_color='lightgreen',font_size='30sp',bold=True, group='apprence', size=(0.2,1),
                         pos_hint={"right": 1, "top": .90})
        ap3.id = 2

        ap4 = ToggleButton(text='Sunset',on_press=self.fr_theme,color='tomato',background_color='orangered',font_size='27sp',bold=True, group='apprence', size=(0.2,1),
                         pos_hint={"right": 1, "top": .90})
        ap4.id = 3

        ap5 = ToggleButton(text='Raspberry',on_press=self.fr_theme,color='tomato',background_color='crimson',font_size='18sp',bold=True,group='apprence',size=(0.2,1),
                        pos_hint={"right": 1, "top": .90})
        ap5.id = 4

        self.aprence.add_widget(ap1)
        self.aprence.add_widget(ap2)
        self.aprence.add_widget(ap3)
        self.aprence.add_widget(ap4)
        self.aprence.add_widget(ap5)


    def fr_theme(self, instance):
        theme_id = instance.id
        theme(theme_id)
        savedexport()



    def goback(self,instance):
        app = App.get_running_app()
        app.sm.remove_widget(app.sm.get_screen('main'))
        app.sm.add_widget(Mainscreen(name='main'))
        self.manager.current = 'main'







# main class-------------------------------------------------------------------------------------------------

class Mainapp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Mainscreen(name="main"))
        self.sm.add_widget(Tagscreen(name="first"))
        self.sm.add_widget(Settingscreen(name="setting"))
        return self.sm

if __name__ == "__main__":
    Mainapp().run()