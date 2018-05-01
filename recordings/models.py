from django.db import models

# Create your models here.

class Recordings(models.Model):
	#记录
	seq = models.AutoField(primary_key=True)
	date = models.DateTimeField()
	type = models.CharField(max_length=20)
