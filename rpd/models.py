from django.db.models import Model, CASCADE, CharField, ForeignKey


class EducationPlan(Model):
    """Учебный план"""

    plan = ForeignKey(
        "base.EducationPlan", verbose_name="учебный план", on_delete=CASCADE
    )
    code = CharField("код", max_length=10)
    name = CharField("название", max_length=50)

    class Meta:
        verbose_name = "рабочая программа дисциплины"
        verbose_name_plural = "рабочая программа дисциплины"
