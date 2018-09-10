from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Movie(models.Model):
    source_id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return 'ID: ' + self.source_id

    def save(self, *args, **kwargs):
        # movie ID has to be unique (should probably make it a primary key)
        if Movie.objects.filter(source_id = self.source_id).exists():
            raise ValueError('The movie with ID %s is already present' % self.source_id)
        else:
            # save
            super(Movie, self).save(*args, **kwargs)