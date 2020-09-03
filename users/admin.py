from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active')

    def active(self, obj): 
        return obj.is_active == 1
  
    active.boolean = True

admin.site.register(User, UserAdmin)
