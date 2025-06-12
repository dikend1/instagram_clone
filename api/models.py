from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/")
    biography = models.CharField(max_length=200)
    followers = models.ManyToManyField("self",symmetrical=True,blank=True)
    #
    # @property
    # def friends(self) -> list["User"]:
    #     friends = self.followers.filter(fol)

class Post(models.Model):
    title = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    media_url = models.FileField(upload_to='media/')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def like(self):
        self.likes += 1
        self.save()

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    reply_to = models.ForeignKey("self",on_delete=models.CASCADE,related_name='replies')
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255)

    def like(self):
        self.likes += 1
        self.save()
