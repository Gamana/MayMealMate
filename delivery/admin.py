from django.contrib import admin

# Register your models here.
from .models import User
from .models import Restaurant
from .models import Item

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Item)