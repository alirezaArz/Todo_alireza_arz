def edittagresult(self, tag_id):
    self.clear_widgets()
    global tags
    self.add_widget(Button(text="go back", size=(dp(100), dp(50)), size_hint=(None, None),
                           pos_hint={"right": 1, "top": 0.99}, background_color='darkcyan', background_normal="",
                           on_press=self.editback))

    self.labeltx = TextInput(hint_text=f"{tags[tag_id][0]}", halign='center', font_size='20sp',
                             pos_hint={"right": 0.80, "top": 0.98},
                             size=(dp(500), dp(40)), size_hint=(None, None), background_color='aquamarine',
                             background_normal="", multiline=False)
    self.add_widget(self.labeltx)

    self.descriptiontx = TextInput(hint_text=f"{tags[tag_id][1]}", halign='center', font_size='20sp',
                                   pos_hint={"right": 0.64, "top": 0.85},
                                   size=(dp(500), dp(430)), size_hint=(None, None), background_color='aquamarine',
                                   background_normal="", multiline=True)
    self.add_widget(self.descriptiontx)

    self.savepool = Button(text="save", size=(dp(80), dp(40)), size_hint=(None, None),
                           pos_hint={"right": 0.55, "top": 0.1}, background_color='darkcyan', background_normal="",
                           on_press=self.saveback)
    self.savepool.id = tag_id
    self.add_widget(self.savepool)


    def saveback(self,instance):
        tag_id = instance.id
        bk_saveedits(tag_id, self.labeltx.text, self.descriptiontx.text, self.timetx.text, self.datetx.text, self.tagtx.text)
        self.makegridscreen()

    def editback(self,instance):
        self.clear_widgets()
        self.makegridscreen()

    def preparetoedit(self,instance):
        todo_id = instance.id
        self.uppercl.edittodoresult(todo_id)