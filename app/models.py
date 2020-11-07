from django.db import models
from embed_video.fields import EmbedVideoField


class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    video = EmbedVideoField()
