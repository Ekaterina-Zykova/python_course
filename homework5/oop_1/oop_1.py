"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from typing import Optional


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return self.deadline + self.created > datetime.datetime.now()


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework) -> Optional[Homework]:
        if homework.is_active():
            return homework
        else:
            print("You are late")
            return None


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, days: int) -> Homework:
        return Homework(text, days)
