# Generated by Django 4.2.1 on 2023-06-02 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EducationPlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10, verbose_name="код")),
                ("name", models.CharField(max_length=50, verbose_name="название")),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.educationplan",
                        verbose_name="учебный план",
                    ),
                ),
            ],
            options={
                "verbose_name": "рабочая программа дисциплины",
                "verbose_name_plural": "рабочая программа дисциплины",
            },
        ),
    ]