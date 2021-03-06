from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')

admin.site.register(User, UserAdmin)
