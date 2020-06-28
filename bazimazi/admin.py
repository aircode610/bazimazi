from django.contrib import admin

from .models import User, Ad, Type, State, Category

# Register your models here.

admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Type)
admin.site.register(State)
admin.site.register(Category)
