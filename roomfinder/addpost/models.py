from django.db import models

# Create your models here.
class Add(models.Model):
	Location = models.TextField()
	pdf = models.FileField(upload_to = "pic/pdfs")
	Price = models.TextField()