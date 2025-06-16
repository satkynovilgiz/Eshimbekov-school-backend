from django.db import models

class AboutBlock(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Текст")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"
