from django.contrib import admin

from proxy.models import Speed


@admin.register(Speed)
class SpeedModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'provider',
        'elapsed_time',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'provider',
    )

    inlines = (
    )

    search_fields = (
        'provider',
    )

    readonly_fields = (
        'provider',
        'elapsed_time',

        'created_at',
        'updated_at',
    )
