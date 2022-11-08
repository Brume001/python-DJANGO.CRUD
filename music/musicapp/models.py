from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.CharField(max_length=400)


    def __str__(self):
        return self.first_name
    
class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length=400)

    def __str__(self):
        return self.title
    

class Lyrics(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    song_id = models.CharField (max_length=400)

    def __str__(self):
        return self.song_id
    
