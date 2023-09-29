from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    auther = models.CharField(max_length=100,unique=True, default=True)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to='images/blog', blank=True,default=None)
    date = models.DateTimeField(auto_now_add=True)
    blog_slug = AutoSlugField(populate_from='title', default=None, unique=True)

class HomeSlider(models.Model):
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='images/homeslider', blank=True,default=None)
