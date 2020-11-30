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
            Wrapper.counter += 1

        @classmethod
        def get_created_instances(cls) -> int:
            return Wrapper.counter

        @classmethod
        def reset_instances_counter(cls) -> int:
            last_counter = Wrapper.counter
            Wrapper.counter = 0
            return last_counter

    return Wrapper
