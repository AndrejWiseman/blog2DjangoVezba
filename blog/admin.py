from django.contrib import admin

from . import models


# Register your models here.


#sta da se vidi, koje polje u admin post
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')


admin.site.register(models.Post, AuthorAdmin)
