import imp
from django.contrib import admin
from .models import correspondencia
from .models import residencia

# Register your models here.
 
admin.site.register(correspondencia)
admin.site.register(residencia)