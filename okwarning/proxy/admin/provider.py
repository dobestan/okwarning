from django.contrib import admin

from proxy.models import Provider


@admin.register(Provider)
class ProviderModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
