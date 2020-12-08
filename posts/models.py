from django.db import models

# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to="album/image", null=True, blank=True)

	def __str__(self):
		return self.title

class AlbumImages(models.Model):
	album = models.ForeignKey(Album, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="album/images", null=True, blank=True)

	def __str__(self):
		return self.Album.title		