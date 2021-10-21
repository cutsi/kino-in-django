from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.db import fields

class Projekcija(models.Model):
    ime_filma = models.CharField(max_length=200)
    vrijeme_filma = models.DateTimeField(default = timezone.now)
    kapacitet_dvorane = models.IntegerField()
    broj_prodanih_karata = models.IntegerField(default=0)
    def __str__(self):
        return (self.ime_filma)

class Karta(models.Model):
    broj_sjedala = models.CharField(max_length=10)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    projekcija = models.ForeignKey(Projekcija,on_delete = models.CASCADE)

    def __str__(self):
        return (self.broj_sjedala)
SEAT_A1 = 'A1'
SEAT_A2 = 'A2'
SEAT_A3 = 'A3'
SEAT_B1 = 'B1'
SEAT_B2 = 'B2'
SEAT_B3 = 'B3'
SEAT_CHOICE = [
    (SEAT_A1, 'A1'),
    (SEAT_A2, 'A2'),
    (SEAT_A3, 'A3'),
    (SEAT_B1, 'B1'),
    (SEAT_B2, 'B2'),
    (SEAT_B3, 'B3'),
    ]
        
class Tickets(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    projekcija = models.ForeignKey(Projekcija,on_delete = models.CASCADE)
    seat_number = models.CharField(max_length = 20, default="NONE")


    broj_sjedala = models.CharField(
        max_length=10,
        choices=SEAT_CHOICE,
        default="NONE",
    )
    def __str__(self):
        return (self.projekcija.ime_filma)
