from django.db import models


class Dht (models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.temp)
