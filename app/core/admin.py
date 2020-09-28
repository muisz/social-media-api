from django.contrib import admin

from core.models.userModels import Profile
from core.models.postModels import Post, Comment, Tag

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
