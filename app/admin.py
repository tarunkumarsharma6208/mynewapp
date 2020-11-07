from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item


class ModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('name', 'video',)


admin.site.register(Item, ModelAdmin)
