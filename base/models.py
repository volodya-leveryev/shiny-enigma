"""Базовые модели данных"""
from django.db.models import Model, CharField, FileField


class EducationPlan(Model):
    """Учебный план"""

    code = CharField("код", max_length=10)
    name = CharField("название", max_length=50)
    file = FileField("файл")

    class Meta:
        verbose_name = "учебный план"
        verbose_name_plural = "учебные планы"
