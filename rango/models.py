from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


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
    slug = models.SlugField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length = Max_Length, unique=True)
    picture = models.ImageField(upload_to='Munro_Images', blank=True)
    difficulty = models.IntegerField(default = 0)
    elevation = models.IntegerField(default = 0)
    coordinates = models.CharField(max_length = Max_Length, default = "")
    description = models.CharField(max_length = 2048, default = "")
    image_1 = models.CharField(max_length = Max_Length, unique=True)
    image_2 = models.CharField(max_length = Max_Length, unique=True)
    image_3 = models.CharField(max_length = Max_Length, unique=True)
    #munroarea = models.ForeignKey(Area, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Munro, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural='Munros'

    def __str__(self):
        return self.name

class BaggedMunros(models.Model):
    hiker_key = models.ForeignKey('Hiker', on_delete=models.CASCADE, null=True, blank=True)
    munro = models.ForeignKey(Munro, on_delete=models.CASCADE,null=True ,blank=True)

    class Meta:
        verbose_name_plural='Bagged Munros'

    def __str__(self):
        return self.munro.name
        
class Hiker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bagged =  models.CharField(max_length = 300, default='', blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def bagged_as_list(self):
        return self.bagged.split(',')

    class Meta:
        verbose_name_plural='Hikers'

class Report(models.Model):

    author = models.OneToOneField(Hiker, on_delete=CASCADE)
    munro = models.ForeignKey(Munro, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to ='report_images', blank = True)
    difficulty = models.IntegerField(default = 0)
    report_text = models.CharField(max_length = 3000)
    difficulty = models.IntegerField(default = 0, validators=[MaxValueValidator(10), MinValueValidator(1)])
    #date = models.DateTimeField(null=True, blank=True)


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
