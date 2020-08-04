from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Writer(models.Model):
    first_name = models.CharField(max_length=30,default=True)
    last_name = models.CharField(max_length=30,default=True)
    email = models.EmailField(default=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE,default=None,null=False)
    text= models.TextField(max_length=400 )
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.text   

class Video(models.Model):
     
    title=models.CharField( max_length=50)
    description=models.TextField(blank=True)
    url=models.URLField( max_length=200)
    date=models.DateField(auto_now=True)
    comments=models.ForeignKey(Comment, default=True,on_delete=models.CASCADE,blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=None,null=False)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.title