from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="redactor_set",
        related_query_name="redactor",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="redactor_set",
        related_query_name="redactor",
    )

    class Meta:
        ordering = ("username", "-years_of_experience")

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
