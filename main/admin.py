# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Education, Project, Contact

admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Contact)
