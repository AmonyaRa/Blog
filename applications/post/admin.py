from django.contrib import admin

from applications.post.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
