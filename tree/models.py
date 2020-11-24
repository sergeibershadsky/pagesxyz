from django.db import models


class Page(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, unique=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
