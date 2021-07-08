from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    ngo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
    
# class Category(models.Model):
#     name = models.CharField(max_length = 100)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("post-detail", kwargs={"pk": self.pk})

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 100, default='ventilator')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

class Donation(models.Model):
    receiver = models.CharField(max_length = 100)
    donor = models.CharField(max_length = 100)
    quantity = models.IntegerField(default = 1)
    category = models.CharField(max_length = 100)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.donor
# Create your models here.
