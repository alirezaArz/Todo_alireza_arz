from kivy.app import App
from kivy.uix.button import Button
from kivy.metrics import dp

class HGFHH(Button):
    button = Button(
        text="Rounded Button",
        size_hint=(None, None),
        size=(dp(15), dp(15)),
        background_normal='',  # حذف تصویر پیش‌فرض
        background_color=(0.3, 0.6, 0.9, 1),  # رنگ دلخواه
    )
    button.border = [50, 50, 50, 50]  # تنظیم گردی گوشه‌ها



class mainapp(App):
    def build(self):
        return HGFHH()

if __name__ == '__main__':
    mainapp().run()