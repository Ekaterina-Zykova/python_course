import datetime

import pytest

from homework5.oop_1.oop_1 import Homework, Student, Teacher


def test_init_teacher():
    teacher = Teacher("Daniil", "Shadrin")
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_init_student():
    student = Student("Roman", "Petrov")
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


@pytest.mark.parametrize(
    ["text", "deadline"],
    [
        ("test1", 0),
        ("test2", 5),
    ],
)
def test_create_homework(text: str, deadline: int):
    test_homework = Homework(text, deadline)
    assert test_homework.created == datetime.datetime.now()
    assert test_homework.deadline == datetime.timedelta(days=deadline)
    assert test_homework.text == text


def test_do_homework(capsys):
    student = Student("Roman", "Petrov")
    homework_on_time = Homework("test1", 5)
    homework_late = Homework("test2", 0)
    assert student.do_homework(homework_on_time) is homework_on_time
    assert (
        student.do_homework(homework_late) is None
        and capsys.readouterr().out.strip() == "You are late"
    )
