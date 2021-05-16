from django.contrib import admin
from api.models import LongRunningTask

# Register your models here.


class LongRunningTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'created_at', 'updated_at')


admin.site.register(LongRunningTask, LongRunningTaskAdmin)
