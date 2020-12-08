from django.contrib import admin
from .models import Album, AlbumImages

# Register your models here.

class AlbumImagesAdmin(admin.StackedInline):
	model =AlbumImages

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	inline = [AlbumImagesAdmin]

	class Meta:
		model = Album	

@admin.register(AlbumImages)
class AlbumImagesAdmin(admin.ModelAdmin):
	pass

