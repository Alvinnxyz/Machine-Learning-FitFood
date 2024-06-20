from django.db import models

class Nutrition(models.Model):
    id = models.IntegerField(primary_key=True)
    calories = models.IntegerField()
    proteins = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    name = models.CharField(max_length=512)
    image = models.CharField(max_length=512)

    def __str__(self):
        return self.name
