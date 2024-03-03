from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=100) #Başlık
    content=models.TextField(max_length=500) #İçerik
    image=models.FileField(upload_to="postImage",null=True,blank=True) #Fotoğraf
    published=models.DateField(auto_now_add=True)
    postOwner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title+ " / "+self.postOwner.username
    
class Comment(models.Model):
    content=models.TextField(max_length=300,verbose_name="Your Comment")
    published=models.DateField(auto_now_add=True)
    commentPost=models.IntegerField(default=0)
    commentOwner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.content+" by "+self.commentOwner.username