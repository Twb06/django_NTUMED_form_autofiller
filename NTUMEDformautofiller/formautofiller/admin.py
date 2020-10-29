from django.contrib import admin

# Register your models here.
from .models import Preference, Student, Form

admin.site.register(Preference)
admin.site.register(Student)
admin.site.register(Form)