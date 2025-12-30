from django.contrib import admin
from pull.models import Contact #? I imported Contact from this path
admin.site.register(Contact) #? I registered Contact
# Register your models here.
