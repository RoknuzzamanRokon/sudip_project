from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254)
    upload_Image = models.ImageField(upload_to ='uploads/')
    geeks_field = models.DateField(help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
  
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title