from django.db import models
from django.utils import timezone

class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    tavsifi = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

class Buyurtma(models.Model):
    buyurtma_raqami = models.CharField(max_length=100)
    buyurtma_sanasi = models.DateField(default=timezone.now)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    mahsulot_soni = models.PositiveIntegerField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    amalga_oshirilgan = models.BooleanField(default=False)
    qabul_qilindi = models.BooleanField(default=False)

class Chegirma(models.Model):
    mahsulot = models.OneToOneField(Mahsulot, on_delete=models.CASCADE)
    chegirma_foizi = models.DecimalField(max_digits=5, decimal_places=2)
    chegirma_muddati = models.DateField()

