from django.contrib import admin

from applications.post.models import *


class ImageAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_nu = 10


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin
    ]
    list_display = ['id', 'title', 'post_count_like']

    def post_count_like(self, obj):
        return obj.likes.filter(like=True).count()


# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Image)
