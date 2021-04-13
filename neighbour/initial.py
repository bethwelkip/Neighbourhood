from .models import Users, Contact, Business, Neighbourhood, Post

def initialize():
    x = "cont"
    for i in range(4):
        name =  x*i
        post = Post(title = name, text = name*3)
        post.save()
        # cont = Contact(name = name, email = f'{name}@{name}.com')
        # business = Business(name = name, email = f'{name}@{name}.com', services = name*2)
        # cont.save()
        # business.save()
    