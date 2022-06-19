from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Playground(Widget):
    fruit = ObjectProperty(None)
    snake = ObjectProperty(None)


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