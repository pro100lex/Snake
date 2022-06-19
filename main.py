from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, BooleanProperty


class Playground(Widget):
    fruit = ObjectProperty(None)
    snake = ObjectProperty(None)

    # Размер сетки
    col_numb = 16
    row_numb = 8

    # Игровые переменные
    score = NumericProperty(0)
    turn_counter = NumericProperty(0)
    fruit_rythme = NumericProperty(0)

    # Обработка входных данных
    touch_start_pos = ListProperty()
    action_triggered = BooleanProperty(False)


class Fruit(Widget):
    pass


class Snake(Widget):
    head = ObjectProperty(None)
    tail = ObjectProperty(None)


class SnakeHead(Widget):
    pass


class SnakeTail(Widget):
    pass


class SnakeApp(App):
    def build(self):
        game = Playground()
        return game


if __name__ == '__main__':
    SnakeApp().run()