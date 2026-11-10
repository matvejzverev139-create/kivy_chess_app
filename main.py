from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class ChessOverlayApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Заголовок
        root.add_widget(Label(text="Chess Assistant Overlay", font_size='22sp', size_hint=(1, 0.1)))
        
        # Поле для ввода FEN / позиции
        self.fen_input = TextInput(text="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 
                                   size_hint=(1, 0.15), multiline=False)
        root.add_widget(self.fen_input)
        
        # Вывод хода движка
        self.output_label = Label(text="Лучший ход: Едет анализ...", font_size='18sp', size_hint=(1, 0.4))
        root.add_widget(self.output_label)
        
        # Кнопка анализа
        btn = Button(text="АНАЛИЗИРОВАТЬ ПОЗИЦИЮ", size_hint=(1, 0.2), background_color=(0.1, 0.6, 0.3, 1))
        btn.bind(on_press=self.analyze_position)
        root.add_widget(btn)
        
        return root

    def analyze_position(self, instance):
        fen = self.fen_input.text
        # Сюда позже подключим движок / запросы
        self.output_label.text = f"Анализ FEN:\n{fen}\nРекомендация: e2e4"

if __name__ == '__main__':
    ChessOverlayApp().run()
