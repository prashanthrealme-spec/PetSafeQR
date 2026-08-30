from django.contrib import admin
from .models import OwnerProfile


@admin.register(OwnerProfile)
class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'area')
    search_fields = ('user__username', 'user__email', 'phone')