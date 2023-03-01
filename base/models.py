from django.db import models

class App(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name