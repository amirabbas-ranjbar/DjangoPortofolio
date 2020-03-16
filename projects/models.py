from django.db import models
from personal_portfolio import settings
import os


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    # image = models.FilePathField(path=os.path.join(settings.BASE_DIR, 'projects/static/img'))
    # image = models.FilePathField(path="/img")
    # image = models.FileField(upload_to="projects/static/img/")
    image = models.ImageField(upload_to='projects/static/img')