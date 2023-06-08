"""Базовые модели данных"""
from django.db.models import Model, CharField, FileField


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
    file = FileField("файл")

    class Meta:
        verbose_name = "учебный план"
        verbose_name_plural = "учебные планы"

    def __str__(self):
        return f"{self.code} {self.name}"