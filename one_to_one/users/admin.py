from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


# Определим описание для встраивания в админку
class ProfileInlined(admin.TabularInline):
    model = Profile
    can_delete = False


# Определим новый вид UserAdmin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlined,)


# Перерегистрируем UserAdmin
# Это позволит использовать админку с дополнительными полями вместо штатной
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
