def donenew(self, getting_label, ids):
    self.made_layout = BoxLayout()

    dbtn = Button(text="remove", background_color='darkcyan', background_normal="", size_hint=(.1, .7))
    dbtn.id = ids

    xbtn = Button(text="remove", background_color='darkcyan', background_normal="", size_hint=(.1, .7))
    xbtn.id = ids

    nbtn = (Button(text=f"{getting_label}", font_size='30sp', background_color='lightseagreen', background_normal="",
                   size_hint=(1, .7)))
    nbtn.id = ids


    self.made_layout.add_widget(dbtn)
    self.made_layout.add_widget(xbtn)
    self.made_layout.add_widget(nbtn)
    self.made_layout.size_x = 1
    self.made_layout.size_hint_y = None
    self.made_layout.size_y = dp(5)
    self.add_widget(self.made_layout)