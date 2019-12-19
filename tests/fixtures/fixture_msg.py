import pytest


class MsgError:

    def __init__(self, method_name, *args, **kwargs):
        self.result = getattr(self, method_name)(*args, **kwargs)

    def add_class(self, class_name, child=False, parent_name=''):
        text = f'Добавьте класс `{class_name}`'
        if child:
            text += f', этот класс наследуется от класса `{parent_name}`'
        return text

    def add_method(self, method_name, class_name):
        return f'Добавьте метод `{method_name}()` для класса `{class_name}`'

    def wrong_method(self, method_name, class_name):
        return f'Проверьте правильность работы метода `{method_name}()` у класса `{class_name}`'

    def dont_create_method(self, method_name, class_name):
        return f'`Метод `{method_name}()` не должен быть создан для класса `{class_name}`'

    def add_attr(self, attr_name, class_name):
        return f'Добавьте свойство `{attr_name}` классу `{class_name}`'

    def wrong_attr(self, attr_name, class_name, msg=''):
        return f'Неверное значение свойства `{attr_name}` у класса `{class_name}`{msg}'

    def dont_create_attr(self, attr_name, class_name):
        return f'`Свойство `{attr_name}` не должен быть создано для класса `{class_name}`'

    def child_method(self, child_name, parent_name):
        return f'`{child_name}` класс наследуется от класса `{parent_name}`'


@pytest.fixture
def msg_err():
    def _msg_err(msg_name, *args, **kwargs):
        msg = MsgError(msg_name, *args, **kwargs)
        return msg.result
    return _msg_err
