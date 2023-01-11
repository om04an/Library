from django.db import models
from django_resized import ResizedImageField


class Book(models.Model):
    name = models.CharField(max_length=250)
    image = ResizedImageField(size=[217, 342], crop=['top', 'left'], upload_to='static/Home_files/media/images')
    date = models.DateField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.name
