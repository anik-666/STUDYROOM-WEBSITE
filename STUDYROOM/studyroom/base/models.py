from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add any additional fields you want to include in the User model
    
    name = models.CharField(max_length=200,unique=True,blank=True)
    username = models.CharField(max_length=200, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
class Topic(models.Model):
    
    name = models.CharField(max_length=200, null=False,)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)

class Room(models.Model):

    
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=False, blank= False)
    description = models.TextField(null= True, blank= True,)
    participants = models.ManyToManyField(User, related_name='participants', blank= True)
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add= True)
    objects = models.Manager()
    

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return str(self.name)
    
class Messages(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add= True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return str(self.body)