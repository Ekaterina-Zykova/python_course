"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    class Wrapper(cls):
        counter = 0

        def __init__(self):
            super().__init__()
            cls.counter += 1

        @classmethod
        def get_created_instances(cls) -> int:
            return cls.counter

        @classmethod
        def reset_instances_counter(cls) -> int:
            last_counter = cls.counter
            cls.counter = 0
            return last_counter

    cls = Wrapper
    return cls


@instances_counter
class User:
    pass
