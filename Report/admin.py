from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Report, RepairRequest
from .models import OpdUser

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity']
    search_fields = ['name']

@admin.register(RepairRequest)
class RepairRequestAdmin(SimpleHistoryAdmin):  
    list_display = [
        'request_id', 'category', 'sub_item', 'department',
        'device_code','remark', 'status_user', 'status', 'unknown_device','reported_by','assigned_to', 'created_at'
    ]
    list_filter = ['category', 'status', 'status_user', 'created_at']
    search_fields = ['request_id', 'detail', 'department', 'device_code']
    readonly_fields = ['request_id', 'created_at']
    ordering = ['-created_at']

    fieldsets = (
        ('ข้อมูลแจ้งซ่อม', {
            'fields': ('request_id', 'category', 'sub_item', 'detail','remark', 'department', 'device_code', 'unknown_device')
        }),
        ('สถานะ', {
            'fields': ('status_user', 'status','reported_by','assigned_to',)
        }),
        ('ระบบ', {
            'fields': ('created_at', 'in_progress_at','repairclaim_at', 'completed_at')
            
        }),
    )

@admin.register(OpdUser)
class OpdUserAdmin(admin.ModelAdmin):
    list_display = ('loginname', 'name')
    search_fields = ('loginname', 'name')  