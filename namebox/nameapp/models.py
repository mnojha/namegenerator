from django.db import models

# Create your models here.
class Namelist(models.Model):
	human_name = models.CharField(max_length=200)
	