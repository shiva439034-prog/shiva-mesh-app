from kivy.app import App
from kivy.uix.label import Label

class ShivaMeshApp(App):
    def build(self):
        return Label(text='Shiva Mesh Factory Live!')

if __name__ == '__main__':
    ShivaMeshApp().run()
