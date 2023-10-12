from django.contrib import admin

from mainapp.models import User, AdminUser, ManagerUser, BasicUser

admin.site.register(User)
admin.site.register(AdminUser)
admin.site.register(ManagerUser)
admin.site.register(BasicUser)