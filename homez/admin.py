from django.contrib import admin
from .models import Comment, Likes, Profile, Nyumbani
# Register your models here.


admin.site.register(Profile)
admin.site.register(Nyumbani)
admin.site.register(Likes)
admin.site.register(Comment)

