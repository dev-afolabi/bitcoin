from django.contrib import admin
from .models import User
from image_cropping import ImageCroppingMixin

# Register your models here.
class UserAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
