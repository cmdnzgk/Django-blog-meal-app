from django.db import models

class Post(models.Model):
    baslik = models.CharField(max_length=100)
    icerik = models.TextField()

    def __str__(self):
        return self.baslik