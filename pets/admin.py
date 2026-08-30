from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'pet_type',
        'owner',
        'gender',
        'status',
        'created_at',
    )

    list_filter = (
        'pet_type',
        'gender',
        'status',
    )

    search_fields = (
        'name',
        'breed',
        'owner__username',
    )

    readonly_fields = (
        'pet_id',
        'created_at',
        'updated_at',
    )