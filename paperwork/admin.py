from django.contrib import admin

from paperwork import models


class EducationPlanAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "name",
        "qualification",
        "short",
        "comment",
    ]


class StudyGroupAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "edu_plan",
    ]


admin.site.register(models.EducationPlan, EducationPlanAdmin)
admin.site.register(models.StudyGroup, StudyGroupAdmin)
admin.site.register(models.SubjectPlan)
admin.site.register(models.Teacher)
admin.site.register(models.TeacherSubject)
