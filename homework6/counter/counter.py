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
    setattr(cls, "counter", 0)

    def counter_init(self):
        cls.counter += 1

    def get_created_instances(*args, **kwargs) -> int:
        return cls.counter

    def reset_instances_counter(*args, **kwargs) -> int:
        last_counter = cls.counter
        cls.counter = 0
        return last_counter

    setattr(cls, "__init__", counter_init)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls


@instances_counter
class User:
    pass
