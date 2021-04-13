from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank = True)
    is_admin = models.BooleanField(default=False)
class Admin(models.Model):
    user = models.ForeignKey(to=Users, on_delete = models.CASCADE)

class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupants = models.IntegerField()
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE)
    def create_neigborhood(name, location, admin):
        neighbor = Neighbourhood(name=name, location = location, occupants = 0, admin = admin)
        neighbor.save()
    def delete_neigborhood():
        pass
    def find_neigborhood(neigborhood_id):
        pass
    def update_neighborhood():
        pass
    def update_occupants():
        pass
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 100,blank = True, null = True)
    facebook = models.CharField(max_length = 100, blank = True, null = True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete = models.CASCADE)


class Business(models.Model):
    name = models.CharField(max_length=100)
    services = models.CharField(max_length=1000)
    email = models.EmailField(max_length = 100)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete = models.CASCADE)
    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    def create_business(name,services,email, user, neighbourhood):
        business = Business(name = name, services = services, email = email, user = user,neighbourhood = neighbourhood)
        business.save()
        return

    def delete_business(name = None, id = None):
        if name is not None:
            business = Business.objects.filter(name = name).first()
            business.delete()
        elif id is not None:
            business = Business.objects.filter(name = name).first()
            business.delete()
        else: 
            return

    def find_business(business_id):
        return Business.objects.filter(id = business_id)
    def search_business(search_term):
        business = Business.objects.filter(name.casefold().__contains__(search_term.casefold())).all()
        return business
    def update_business( old_name, new_name = None,id = None, services = None, email = None):
        if id is not None:
            business = Business.objects.filter(id = id).first()
        else: 
            business = Business.objects.filter(name = old_name).first()
            return
        if new_name is not None:
            business.update(name = new_name)
        if services is not None:
            business.update(services = services)
        if email is not None:
            business.update(email = email)
        business.save()
        return



class Post(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField(editable=True, blank = False)
    user = models.ForeignKey(Users,on_delete = models.CASCADE)
