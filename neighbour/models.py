from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Neighbourhood(models.Model):
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 100,blank = True, null = True)
    facebook = models.CharField(max_length = 100, blank = True, null = True)
    twitter = models.CharField(max_length = 100, blank = True, null = True)
    linkedIn = models.CharField(max_length = 100, blank = True, null = True)
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 100,blank = True, null = True)
    facebook = models.CharField(max_length = 100, blank = True, null = True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete = models.CASCADE)

class Users(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank = True)
    contact = models.ForeignKey(Contact, blank = True, null = True, on_delete = models.DO_NOTHING)

class Business(models.Model):
    name = models.CharField(max_length=100)
    services = models.CharField(max_length=1000)
    email = models.EmailField(max_length = 100)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete = models.CASCADE)
    user = models.ForeignKey(Users,on_delete = models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField(editable=True, blank = False)
    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    def search_projects(search):
        projects = Project.objects.all()
        lis = []
        for project in projects:
            if project.description.casefold().__contains__(search.casefold()) or project.title.casefold().__contains__(search):
                lis.append(project)
        return lis


