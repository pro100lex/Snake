from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, \
    BooleanProperty, OptionProperty, ReferenceListProperty


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
    # Направление головы и координаты
    direction = OptionProperty(
        'Right', options=['Up', 'Down', 'Left', 'Right']
    )
    x_pos = NumericProperty(0)
    y_pos = NumericProperty(0)
    pos = ReferenceListProperty(x_pos, y_pos)

    # Отображение на холсте
    points = ListProperty([0] * 6)
    object_on_board = ObjectProperty(None)
    state = BooleanProperty(False)


class SnakeTail(Widget):
    # Длина хвоста
    size = NumericProperty(3)

    # Переменная для хранения позиций блоков
    blocks_positions = ListProperty()

    # Переменная для хранения объектов хвоста
    tail_blocks_objects = ListProperty()


class SnakeApp(App):
    def build(self):
        game = Playground()
        return game


if __name__ == '__main__':
    SnakeApp().run()