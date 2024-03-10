from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

# Post(models.Model) -> Herança -> classe Post extende Model 
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # limite fixo
    text = models.TextField() # sem limite
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title