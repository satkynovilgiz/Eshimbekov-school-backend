from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
