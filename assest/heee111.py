class TagGridlayout(GridLayout):
    def __init__(self,screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = dp(10)
        self.spacing = dp(-20)
        self.screen_manager = screen_manager
        self.refresh()
        global todo
        for object in todo:
            self.addnew(object[0])

    def refresh(self):
        self.clear_widgets()

    def addnew(self,getting_label):
        self.made_layout.add_widget(Button(text=f"{getting_label}",font_size='30sp', background_color = 'lightseagreen',background_normal = "", size_hint=(1,1)))
        self.made_layout.size_x = 1
        self.made_layout.size_hint_y = None
        self.made_layout.size_y = dp(5)
        self.add_widget(self.made_layout)


# main grid layout's scroll feature
class Scrolltag(ScrollView):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.72)
        self.pos_hint = {"x": 0, "y": 0.1}
        self.taggrid = TagGridlayout(screen_manager, size_hint=(1, None), pos_hint=(0.5, 0.01))
        self.taggrid.bind(minimum_height=self.taggrid.setter('height'))
        self.taggrid.height = self.taggrid.minimum_height
        self.add_widget(self.taggrid)

# main screen
class Tagscreen(Screen):
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
        self.tag_scroll = Scrolltag(self.manager)
        self.add_widget(self.tag_scroll)

        self.add_widget(Button(text="+",font_size='100sp',size=(dp(80),dp(72)),size_hint=(None,None),pos_hint={"right":0.56,"top":0.99}, background_color = 'darkcyan',background_normal = "",on_press=self.maketodoresult))
        self.made_layout.add_widget(Button(text="delete",font_size='100sp',size=(dp(80),dp(72)),size_hint=(None,None),pos_hint={"right":0.56,"top":0.99}, background_color = 'darkcyan',background_normal = ""))

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


        self.add_widget(Button(text="save",on_press=self.saveandexit, size=(dp(80), dp(40)), size_hint=(None, None),
                               pos_hint={"right": 0.55, "top": 0.1}, background_color='darkcyan', background_normal=""))



    def exit(self, instance):
        self.makegridscreen()

    def saveandexit(self,instance):
        bk_addtag(self.labeltx.text, self.descriptiontx.text)
        self.makegridscreen()

    def makegridscreen(self):
        class Mainscreen(Screen):
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
                self.tag_scroll = Scrolltag(self.manager)
                self.add_widget(self.tag_scroll)

                self.add_widget(Button(text="+",font_size='100sp',size=(dp(80),dp(72)),size_hint=(None,None),pos_hint={"right":0.56,"top":0.99}, background_color = 'darkcyan',background_normal = "",on_press=self.maketodoresult))