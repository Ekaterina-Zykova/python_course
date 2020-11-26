import datetime

import pytest

from homework6.oop_2.oop_2 import (
    DeadlineError,
    Homework,
    HomeworkResult,
    Student,
    Teacher,
)


def test_init_teacher():
    teacher = Teacher("Daniil", "Shadrin")
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_init_student():
    student = Student("Roman", "Petrov")
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_create_homework():
    hw = Teacher.create_homework("Learn OOP", 1)
    assert hw.text == "Learn OOP"
    assert hw.created == datetime.datetime.now()
    assert hw.deadline == datetime.timedelta(days=1)


def test_homework_result_with_type_error():
    student = Student("Roman", "Petrov")
    with pytest.raises(TypeError) as exc:
        HomeworkResult(student, "not_a_homework", "solution")
    assert exc.value.args[0] == "You gave a not Homework object"


def test_homework_result_without_error():
    student = Student("Roman", "Petrov")
    homework = Homework("Learn OOP", 1)
    hw_result = HomeworkResult(student, homework, "I have done this hw")
    assert hw_result.author is student
    assert hw_result.homework is homework
    assert hw_result.solution == "I have done this hw"


def test_do_homework_with_error():
    student = Student("Roman", "Petrov")
    homework = Homework("Learn OOP", 0)
    with pytest.raises(DeadlineError) as exc:
        student.do_homework(homework, "solution")
    assert exc.value.args[0] == "You are late"


def test_do_homework_without_error():
    student = Student("Roman", "Petrov")
    homework = Homework("Learn OOP", 5)
    assert isinstance(student.do_homework(homework, "solution"), HomeworkResult)


def test_check_homework_with_true():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    homework = Homework("Learn OOP", 5)
    hw_result = HomeworkResult(student, homework, "I have done this hw")
    assert teacher.check_homework(hw_result) is True


def test_check_homework_with_false():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    homework = Homework("Learn OOP", 5)
    hw_result = HomeworkResult(student, homework, "done")
    assert teacher.check_homework(hw_result) is False


def test_homework_done_have_only_unique_solutions():
    teacher_1 = Teacher("Daniil", "Shadrin")
    teacher_2 = Teacher("Aleksandr", "Smetanin")
    student = Student("Roman", "Petrov")
    homework = Homework("Learn OOP", 5)
    done_homework = HomeworkResult(student, homework, "I have done this hw")
    teacher_1.check_homework(done_homework)
    teacher_2.check_homework(done_homework)
    assert teacher_1.homework_done == teacher_2.homework_done


def test_reset_results():
    student = Student("Roman", "Petrov")
    homework_1 = Homework("Learn OOP", 5)
    hw1_result = HomeworkResult(student, homework_1, "I have done this hw")
    Teacher.check_homework(hw1_result)
    homework_2 = Homework("Read docs", 3)
    hw2_result = HomeworkResult(student, homework_2, "I have done this hw too")
    Teacher.check_homework(hw2_result)
    assert len(Teacher.homework_done) == 2
    assert homework_1 in Teacher.homework_done
    assert homework_2 in Teacher.homework_done
    Teacher.reset_results(homework_1)
    assert homework_1 not in Teacher.homework_done
    assert len(Teacher.homework_done) == 1
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0
