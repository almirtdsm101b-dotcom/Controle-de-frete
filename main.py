from kivy.app import App
from kivy.uix.label import Label


class ControleFretesApp(App):
    def build(self):
        return Label(text="Controle de Fretes")


if __name__ == "__main__":
    ControleFretesApp().run()
    
