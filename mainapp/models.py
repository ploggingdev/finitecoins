from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import datetime
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

class Game(models.Model):
    name = models.CharField(max_length=30, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9 ]+$', "Only lower case, upper case letters, numbers and spaces are allowed")])
    description = models.CharField(max_length=1000, null=True, blank=True)
    description_html = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class StaticResource(models.Model):
    description = models.CharField(max_length=300, null=True, blank=True ,validators=[RegexValidator(r'^[a-zA-Z0-9 ]+$', "Only lower case, upper case letters, numbers and spaces are allowed")])
    url = models.URLField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url