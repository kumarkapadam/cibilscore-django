from django.contrib import admin
from cibilscoreapp.models import Register


# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'salary', 'email', 'mobilenum']


admin.site.register(Register, RegisterAdmin)
