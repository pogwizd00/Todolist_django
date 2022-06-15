from django.contrib import admin
from .models import Todolist
from .models import User
from .models import Item

# Register your models here.

admin.site.register(User)
admin.site.register(Todolist)
admin.site.register(Item)