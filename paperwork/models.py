"""Базовые модели данных"""
from django.db.models import (
    Model, CharField, FileField, ForeignKey, CASCADE, IntegerField
)


QUALIFICATIONS = (
    ("B", "Бакалавриат"),
    ("M", "Магистратура"),
    ("S", "Специалитет"),
)


class EducationPlan(Model):
    """Учебный план"""

    code = CharField("код", max_length=10)
    name = CharField("название", max_length=50)
    qualification = CharField("квалификация", max_length=1,
                              choices=QUALIFICATIONS)
    year = IntegerField("год поступления")
    file = FileField("файл")

    class Meta:
        verbose_name = "учебный план"
        verbose_name_plural = "учебные планы"

    def __str__(self):
        return f"{self.code} {self.name}"


class SubjectPlan(Model):
    """Рабочая программа дисциплины"""

    plan = ForeignKey("EducationPlan", verbose_name="учебный план",
                      on_delete=CASCADE)
    code = CharField("код", max_length=10)
    name = CharField("название", max_length=50)
    file = FileField("файл")

    class Meta:
        verbose_name = "рабочая программа дисциплины"
        verbose_name_plural = "рабочие программы дисциплин"

    def __str__(self):
        return f"{self.code} {self.name}"
