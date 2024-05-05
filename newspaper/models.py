from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ("username", "years_of_experience")

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    published_date = models.DateTimeField()
    topics = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers", blank=True)

    class Meta:
        ordering = ("-published_date",)

    def __str__(self):
        return self.title
