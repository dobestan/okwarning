from django.contrib import admin

from proxy.models import History


@admin.register(History)
class HistoryModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'url',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
        'url',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
