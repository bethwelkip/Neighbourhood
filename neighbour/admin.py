from django.contrib import admin
from .models import Users, Neighbourhood, Contact, Admin, Business, Post
from django.contrib.auth.models import User

admin.site.register(Users)
admin.site.register(Admin)
admin.site.register(Neighbourhood)
admin.site.register(Contact)
admin.site.register(Business)
admin.site.register(Post)
# Register your models here.
