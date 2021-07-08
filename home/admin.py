from django.contrib import admin
from .models import Profile, Contact, Post,Donation
#Category
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Post)
#admin.site.register(Category)
admin.site.register(Donation)

# Register your models here.
