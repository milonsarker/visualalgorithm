from django.db import models

# Create your models here.
class SortingAlgorithm(models.Model):
    algoName = models.CharField(max_length=50)
    algoComplexity = models.CharField(max_length=50)
    algoDetails = models.CharField(max_length=2000)
