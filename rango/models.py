from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


Max_Length = 128 #default max length

class Area(models.Model): #geographic area where a munro exists
    name = models.CharField(max_length=Max_Length, unique = True) #area name
    slug = models.SlugField() #slug for areas name
    views = models.IntegerField(default=0) #views of area
    likes = models.IntegerField(default=0) #likes of area
    
    def save(self, *args, **kwargs):  #save a created area to DB
        self.slug = slugify(self.name)

        #ensure non valid values for views/likes removed 
        if self.views < 0 :
            self.views = 0
        if self.likes < 0:
            self.likes = 0
        super(Area, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural='Areas'

    def __str__(self):
        return self.name

class Munro(models.Model): #model for the munro mountain
    area = models.ForeignKey(Area, on_delete=models.CASCADE) #linnk to the area object
    name = models.CharField(max_length = Max_Length, unique=True) #munro name
    slug = models.SlugField() #slugged v/ of name
    difficulty = models.IntegerField(default = 0) #munro difficulty
    elevation = models.IntegerField(default = 0) #munro elevation
    coordinates = models.CharField(max_length = Max_Length, default = "") #lat. and long. of munro
    duration = models.CharField(max_length = 2048, default = "") #walk length (hours)
    length = models.IntegerField(default = 0) #walk length (km)
    description = models.CharField(max_length = 2048, default = "") #text description
    views = models.IntegerField(default=0) #number of views
    likes = models.IntegerField(default=0) #number of likes
    mapslink = models.CharField(default="", max_length=2048) #url for google maps embed


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.views < 0 :
            self.views = 0
        if self.likes < 0:
            self.likes = 0 #as for area, ensure likes/ views valid
        super(Munro, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural='Munros'

    def __str__(self):
        return self.name

class UserLikeArea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    has_liked = models.BooleanField(default=False) #user/ area combination has been liked or not

    def save(self, *args, **kwargs):
        super(UserLikeArea, self).save(*args, **kwargs)

    def __str__(self):
        return self.has_liked

class UserLikeMunro(models.Model):
    munro = models.ForeignKey(Munro, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    has_liked = models.BooleanField(default=False) #user/munro combination has been liked

    def save(self, *args, **kwargs):
        super(UserLikeMunro, self).save(*args, **kwargs)

    def __str__(self):
        return self.has_liked

class BaggedMunros(models.Model): #associate if a user has completed a particualr munro
    hiker_key = models.ForeignKey('Hiker', on_delete=models.CASCADE, null=True, blank=True)
    munro = models.ForeignKey(Munro, on_delete=models.CASCADE,null=True ,blank=True)

    class Meta:
        verbose_name_plural='Bagged Munros'

    def __str__(self):
        return self.munro.name
        
class Image(models.Model): #images associated with a particular munro
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
 
        
class Hiker(models.Model): #extend upon user, with added functionality for the Rango site
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bagged =  models.CharField(max_length = 300, default='', blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    verified = models.BooleanField(default=False)
    munro = models.ForeignKey(Munro, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

    # Required to split bagged field into separate munros
    def bagged_as_list(self):
        return self.bagged.split(',')

    class Meta:
        verbose_name_plural='Hikers'

class Report(models.Model): #text that user uploads about a munro

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to ='report_images', blank = True)
    difficulty = models.IntegerField(default = 0)
    report_text = models.CharField(max_length = 3000)
    difficulty = models.IntegerField(default = 0, validators=[MaxValueValidator(10), MinValueValidator(1)])
    munro = models.ForeignKey(Munro, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name_plural='Reports'

    def __str__(self):
        return self.munro.name + ": " + self.author.username


