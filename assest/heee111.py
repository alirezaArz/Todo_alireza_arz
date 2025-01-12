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

        self.labeltx = TextInput(hint_text="Enter the Label",halign='center',font_size='20sp',pos_hint={"right": 0.80, "top": 0.98},
                                  size=(dp(500), dp(40)), size_hint=(None, None), background_color='aquamarine',background_normal="",multiline=False)
        self.add_widget(self.labeltx)

        self.descriptiontx = TextInput(hint_text="Enter the description",halign='center', font_size='20sp', pos_hint={"right": 0.64, "top": 0.85},
                                  size=(dp(500), dp(430)), size_hint=(None, None), background_color='aquamarine',background_normal="", multiline=True)
        self.add_widget(self.descriptiontx)

        self.datetx = TextInput(hint_text="Date example: 00/00/00 ", font_size='17sp', pos_hint={"right": 0.95, "top": 0.72},
                      size=(dp(200), dp(38)), size_hint=(None, None), background_color='turquoise',background_normal="", multiline=False)
        self.add_widget(self.datetx)

        self.timetx = TextInput(hint_text=" Time example: 00:00:00 ", font_size='17sp',pos_hint={"right": 0.95, "top": 0.80},size=(dp(200), dp(38)),
                                  size_hint=(None, None), background_color='turquoise',background_normal="", multiline=False)
        self.add_widget(self.timetx)

        self.add_widget(Label(text="Enter the date and time ",color='aquamarine', font_size='20sp', pos_hint={"right": 0.95, "top": 0.86},
                      size=(dp(200), dp(38)), size_hint=(None, None)))

        self.add_widget(Label(text="Enter the tag/tags", color='aquamarine',
                              font_size='20sp',pos_hint={"right": 0.95, "top": 0.62},size=(dp(200), dp(38)), size_hint=(None, None)))

        self.tagtx = TextInput(hint_text="existing tags : ",font_size='20sp',pos_hint={"right": 0.97, "top": 0.55},size=(dp(250), dp(250)),
                                  size_hint=(None, None), background_color='turquoise',background_normal="", multiline=True)
        self.add_widget(self.tagtx)

        self.add_widget(Button(text="save", on_press=self.save, size=(dp(80), dp(40)), size_hint=(None, None),
                               pos_hint={"right": 0.55, "top": 0.1}, background_color='darkcyan',background_normal=""))

    def save(self,instance):
        bk_addtodo(self.labeltx.text,self.descriptiontx.text,self.timetx.text,self.datetx.text,self.tagtx.text)
        app = App.get_running_app()
        self.manager.current = 'main'

    def makegridscreen(self, instance):
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




