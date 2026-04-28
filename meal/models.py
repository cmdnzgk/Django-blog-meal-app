from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):

    OGUN_SECENEKLERI = [
        ("kahvalti", "Kahvaltı"),
        ("ogle", "Öğle"),
        ("aksam", "Akşam"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    ad = models.CharField(max_length=100)
    kalori = models.IntegerField()
    miktar = models.CharField(max_length=100)
    aciklama = models.TextField()
    ogun = models.CharField(max_length=20, choices=OGUN_SECENEKLERI)
    created_at = models.DateTimeField(auto_now_add=True)
    protein = models.IntegerField(default=0)
    karbonhidrat = models.IntegerField(default=0)
    yag = models.IntegerField(default=0)

    def __str__(self):
        return self.ad