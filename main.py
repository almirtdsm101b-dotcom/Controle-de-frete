from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=24, spacing=16)

        self.label = Label(
            text="App Kivy Funcionando!",
            font_size="24sp",
        )
        botao = Button(
            text="Toque aqui",
            size_hint_y=None,
            height="56dp",
        )
        botao.bind(on_press=self.ao_clicar)

        layout.add_widget(self.label)
        layout.add_widget(botao)
        return layout

    def ao_clicar(self, instance):
        self.label.text = "Botao clicado com sucesso!"


if __name__ == "__main__":
    MeuApp().run()
    
