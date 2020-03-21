from django.contrib import admin
from .models import CheckInOut, Date

class CheckInOutAdmin(admin.ModelAdmin):
    list_display = ('staff','date_worked', 'check_in', 'check_out', 'overtime_s','overtime_e','total_overtime')


admin.site.register(CheckInOut, CheckInOutAdmin)
admin.site.register(Date)
