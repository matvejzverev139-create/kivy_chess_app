from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ChessOverlayApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        self.label = Label(text="Шахматный помощник запущен", font_size='20sp')
        btn = Button(text="Сделать ход", size_hint=(1, 0.3))
        btn.bind(on_press=self.on_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_click(self, instance):
        self.label.text = "Ход отправлен движку!"

if __name__ == '__main__':
    ChessOverlayApp().run()
