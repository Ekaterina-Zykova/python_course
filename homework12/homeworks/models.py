from datetime import datetime

from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Teacher(Person):
    pass


class Student(Person):
    pass


class Homework(models.Model):
    text = models.TextField(unique=True)
    deadline = models.IntegerField(default=7)
    created = models.DateTimeField(default=datetime.now())
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class HomeworkResult(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField(default=datetime.now())


class HomeworkDone(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
