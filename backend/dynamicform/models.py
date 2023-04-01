from django.db import models

# Create your models here.
class Job(models.Model):
    name_job = models.CharField("Работа", max_length=100)
    release_dates = models.DateField("Release dates")
    due_dates = models.DateField("Due dates")

    def __str__(self):
        return self.name_work

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"