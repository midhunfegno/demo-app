from django.contrib import admin
from DeliveroApp.models import adminregister,driverregister,taskdb
# Register your models here.
admin.site.register(adminregister)
admin.site.register(driverregister)
admin.site.register(taskdb)