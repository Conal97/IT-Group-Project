from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Area(models.Model):
    name = models.CharField(max_length=128, unique = True)

class Munro(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    area = models.CharField(max_length = 128, default = "")
    picture = models.ImageField(upload_to='Munro_Images', blank=True)
    difficulty = models.IntegerField(default = 0)
    elevation = models.IntegerField(default = 0)
    coordinates = models.CharField(default = "")
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Munro, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural='Munros'

    def __str__(self):
        return self.name
        
class Hiker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bagged = models.CharField(default = "")
    picture = models.ImageField(upload_to='profile_images', blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Report(models.Model):
    author = models.OneToOneField(Hiker, on_delete=CASCADE)
    munro = models.ForeignKey(Munro, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to ='report_images', blank = True)
    difficulty = models.IntegerField(default = 0)
    report_text = models.CharField