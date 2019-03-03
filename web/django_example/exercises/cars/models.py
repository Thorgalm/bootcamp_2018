from django.db import models

# Create your models here.

BODY_TYPE_CHOICES = (
    ("sedan", "sedan"),
    ("combi", "combi"),
    ("hatchback", "hatchback"),
    ("cabriolet", "cabriolet"),
    ("van", "van"),
)

ENGINE_TYPE_CHOICES = (
    ("electric", "electric"),
    ("benz", "benz"),
    ("diesel", "diesel"),
    ("steam", "steam"),
    ("hybrid", "hybrid"),
)

class Engine(models.Model):
    type = models.CharField(max_length=20, choices=ENGINE_TYPE_CHOICES)
    power = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type},{self.power}"

class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=50)
    production_year = models.IntegerField()
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES, null=True, blank=True)
    engine = models.ForeignKey(Engine, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand},{self.model},{self.production_year},{self.body_type}"



# tworzymy klasę czyly w django model i chcemy dodac go do bazy danych
# w naszym projekcie domyslna baza danych jest db.sqlite3
# najpierw tworzymy migracje (w konsoli polecenie: makemigration) a potem dorzucamy do bazy danych (w konsoli: migrate, a dokladnie: python manage.py migrate)

