from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from Journal.persons.models import User


class Subject(models.Model):
    """
    Предмет в школьной программе
    """
    name = models.CharField('Название предмета', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'Список предметов'


class SchoolClass(models.Model):
    """
    Список существующих классов в школе
    """
    class_number = models.SmallIntegerField('Цифра')
    class_letter = models.CharField('Буква', max_length=1)
    lessons = models.ManyToManyField(Subject, related_name='grade', verbose_name='Уроки класса')

    def __str__(self):
        return f"{self.class_number}{self.class_letter}"

    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'Список классов'


class GradeStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Grade(models.Model):
    value = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_grades')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.value}"
