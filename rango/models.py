from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


Max_Length = 128

class Area(models.Model):
    name = models.CharField(max_length=Max_Length, unique = True)
    slug = models.SlugField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Area, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Areas'

    def __str__(self):
        return self.name

class Munro(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length = Max_Length, unique=True)
    slug = models.SlugField()
    difficulty = models.IntegerField(default = 0)
    elevation = models.IntegerField(default = 0)
    coordinates = models.CharField(max_length = Max_Length, default = "")
    duration = models.CharField(max_length = 2048, default = "")
    length = models.IntegerField(default = 0)
    description = models.CharField(max_length = 2048, default = "")
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Munro, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural='Munros'

    def __str__(self):
        return self.name

# class UserLikeArea(models.Model):
#     area = models.ForeignKey(Area, on_delete=models.CASCADE,null=True ,blank=True)
#     hiker_key = models.ForeignKey('Hiker', on_delete=models.CASCADE, null=True, blank=True)
#     has_liked = models.BooleanField(default=False)

#     def __str__(self):
#         return self.has_liked

class BaggedMunros(models.Model):
    hiker_key = models.ForeignKey('Hiker', on_delete=models.CASCADE, null=True, blank=True)
    munro = models.ForeignKey(Munro, on_delete=models.CASCADE,null=True ,blank=True)

    class Meta:
        verbose_name_plural='Bagged Munros'

    def __str__(self):
        return self.munro.name
        
class Image(models.Model):
    name = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200, default = "")
    description = models.CharField(max_length = 2048, default = "")
    munro = models.ForeignKey(Munro, related_name='images', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural='Images'

    def __str__(self):
        return self.name
 
        
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

    # author = models.OneToOneField(Hiker, on_delete=CASCADE)
    # munro = models.ForeignKey(Munro, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to ='report_images', blank = True)
    difficulty = models.IntegerField(default = 0)
    report_text = models.CharField(max_length = 3000)
    difficulty = models.IntegerField(default = 0, validators=[MaxValueValidator(10), MinValueValidator(1)])
    #date = models.DateTimeField(null=True, blank=True)
    class Meta:
        verbose_name_plural='Reports'


    def __str__(self):
        return self.munro.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
