from django.db import models

class BloomsTaxonomy(models.Model):
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.level} - {self.name}'