from django.db import models

# Create your models here.
class Room(models.Model):
	address = models.TextField()
	price = models.TextField()
	pdf = models.FileField(upload_to ="room/pdfs")

	def __str__(self):
		return self.address

		