from django.contrib import admin
from .models import User, Role, Characteristics

# Register your models here.
admin.site.register(User)
admin.site.register(Characteristics)
admin.site.register(Role)