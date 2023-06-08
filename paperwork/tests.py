from django.test import TestCase

from paperwork.models import EducationPlan


class TestModelEducationPlan(TestCase):
    """Тесты модели **Учебный план**"""

    def test_str(self):
        code = "09.03.01"
        name = "Информатика и вычислительная техника"
        m = EducationPlan()
        m.code = code
        m.name = name
        s = str(m)
        self.assertEqual(s, f"{code} {name}")
