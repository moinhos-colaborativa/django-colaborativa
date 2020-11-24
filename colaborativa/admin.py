from django.contrib import admin

from colaborativa.models import ExtraInfo


@admin.register(ExtraInfo)
class ExtraInfoModelAdmin(admin.ModelAdmin):
    search_fields = ("user__username", "cpf")
    list_display = (
        "user",
        "cpf",
        "gender",
        "state",
        "city",
    )
