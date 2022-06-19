from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, \
    BooleanProperty, OptionProperty, ReferenceListProperty
from kivy.graphics import Rectangle


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
    # Длительность существования и продолжительность отсутствия
    duration = NumericProperty(10)
    interval = NumericProperty(3)

    # Отображение на поле
    object_on_board = ObjectProperty(None)
    state = BooleanProperty(False)


class Snake(Widget):
    head = ObjectProperty(None)
    tail = ObjectProperty(None)

    def move(self):
        """
            Движение змеи будет происходить в 3 этапа:
            - сохранить текущее положение головы.
            - передвинуть голову на одну позицию вперед.
            - переместить последний блок хвоста на предыдущие координаты головы .
        """
        next_tail_pos = list(self.head.position)
        self.head.move()
        self.tail.add_block(next_tail_pos)

    def remove(self):
        """
            Удаление элементов хвоста и головы
        """
        self.tail.remove()
        self.head.remove()

    def set_position(self, position):
        self.head.pos = position

    def get_position(self):
        """
            Положение змеи равно положению ее головы на поле.
        """
        return self.head.pos

    def get_full_position(self):
        return self.head.pos + self.tail.blocks_positions

    def set_direction(self, direction):
        self.head.direction = direction

    def get_direction(self):
        return self.head.direction


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

    def remove(self):
        # Сброс счетчика длины
        self.size = 3

        # Удаление блоков хвоста
        for block in self.tail_blocks_objects:
            self.canvas.remove(block)

        # Очищение списков объектов хвоста
        self.blocks_positions = []
        self.tail_blocks_objects = []

    def add_block(self, position):
        """
            - Передаем позицию нового блока как аргумент и добавляем блок в список объектов.
            - Проверяем равенство длины хвоста и количества блоков и изменяем, если требуется.
            - Рисуем блоки на холсте, до тех пор, пока количество нарисованных блоков не станет равно длине хвоста.
        """
        # Добавление координат блоков
        self.blocks_positions.append(position)

        # Проверка соответствия количеству блоков
        if len(self.blocks_positions) > self.size:
            self.blocks_positions.pop(0)

        with self.canvas:
            for block_pos in self.blocks_positions:
                x = (block_pos[0] - 1) * self.width
                y = (block_pos[1] - 1) * self.height
                coord = (x, y)
                block = Rectangle(pos=coord, size=(self.width, self.height))

                self.tail_blocks_objects.append(block)

                # Проверка длины
                if len(self.tail_blocks_objects) > self.size:
                    last_block = self.tail_blocks_objects.pop(0)
                    self.canvas.remove(last_block)


class SnakeApp(App):
    game_engine = ObjectProperty(None)

    def build(self):
        self.game_engine = Playground()
        return self.game_engine


if __name__ == '__main__':
    SnakeApp().run()