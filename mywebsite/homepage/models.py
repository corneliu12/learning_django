from django.db import models

class news(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='news/', blank=False)

    def __str__(self):
        return self.title
