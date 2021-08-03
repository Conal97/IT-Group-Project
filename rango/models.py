from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

Max_Length = 128

class Area(models.Model):
    name = models.CharField(max_length=Max_Length, unique = True)
    slug = models.SlugField()   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Area, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Areas'

    def __str__(self):
        return self.name

class Munro(models.Model):
    name = models.CharField(max_length = Max_Length, unique=True)
    area = models.CharField(max_length = Max_Length, default = "")
    picture = models.ImageField(upload_to='Munro_Images', blank=True)
    difficulty = models.IntegerField(default = 0)
    elevation = models.IntegerField(default = 0)
    coordinates = models.CharField(max_length = Max_Length, default = "")
    munroarea = models.ForeignKey(Area, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Munro, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural='Munros'

    def __str__(self):
        return self.name
        
class Hiker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bagged = models.CharField(max_length = Max_Length, default = "")
    picture = models.ImageField(upload_to='profile_images', blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural='Hikers'

class Report(models.Model):

    author = models.OneToOneField(Hiker, on_delete=CASCADE)
    munro = models.ForeignKey(Munro, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to ='report_images', blank = True)
    difficulty = models.IntegerField(default = 0)
    report_text = models.CharField(max_length = 3000)

    def __str__(self):
        return self.munro.name

class Category(models.Model):
    NAME_MAX_LENGTH =128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Page (models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length = TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
