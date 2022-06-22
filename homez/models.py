from html.entities import name2codepoint
from django import forms
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Nyumbani(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    management = models.ForeignKey("profile", on_delete=models.CASCADE, related_name="hood")
    description = models.TextField()
    rooms = models.IntegerField(null=True, blank=True)
    photo=CloudinaryField(blank=True,)
    def __str__(self):
        return self.name

    def create_nyumbani(self):
        self.save()


    def delete_nyumbani(self):
        self.delete()

    @classmethod
    def find_nyumbani(cls, nyumbani_id):
        return cls.objects.filter(id=nyumbani_id)        

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_photo = CloudinaryField('image')
    location = models.CharField(max_length=50, blank=True, null=True)
    nyumbani = models.ForeignKey(Nyumbani, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True)
    image = CloudinaryField('image', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    content=models.TextField(null=True)
    
    def __str__(self):
        return (self.image)
    def save_comment(self):
        self.save()

    # update comments
    def update_comment(self, name):
        self.name = name
        self.save()

     # delete comments from database
    def delete_comments(self):
        self.delete()
class Likes(models.Model):
    nyumbani = models.ForeignKey(Nyumbani,related_name='like_count', null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image
    def save_likes(self):
        self.save()

    # update like
    def update_likes(self, name):
        self.name = name
 
     # delete like from database
    def delete_likes(self):
        self.delete()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'nyumbani'], name="unique_like"),
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        widgets= {
            'content':forms.Textarea(attrs={'rows':2,})
        }
        