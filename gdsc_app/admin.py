from django.contrib import admin
from .models import RegisterGDSC
# Register your models here.


class RegisterGDSCAdmin(admin.ModelAdmin):
    list_display = ('name', 'education', 'whatsapp_number',
                    'email', 'school', 'created_at')
    search_fields = ('name', 'education', 'school')
    list_filter = ('name', 'education')
    ordering = ('name',)


admin.site.register(RegisterGDSC, RegisterGDSCAdmin)
