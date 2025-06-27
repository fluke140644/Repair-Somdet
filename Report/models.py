from django.db import models
from django.db import transaction
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
# Create your models here.

class Report(models.Model): 
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class RepairRequest(models.Model):
    CATEGORY_CHOICES = [
        ('คอมพิวเตอร์', 'คอมพิวเตอร์'),
        ('โปรแกรม', 'โปรแกรม'),
        ('เครื่องปริ้น', 'เครื่องปริ้น'),
        ('อินเตอร์เน็ต', 'อินเตอร์เน็ต'),
    ]

    STATUS_CHOICES = [
        ('pending', 'รอดำเนินการ'),
        ('in_progress', 'กำลังดำเนินการ'),
        ('completed', 'เสร็จสิ้น'),
        ('repairclaim', 'ส่งซ่อม/เคลม'),
        ('cancelled', 'ยกเลิก'),
    ]

    STATUS_CHOICES1 = [
        ('ไม่เร่งด่วน', 'ไม่เร่งด่วน'),
        ('เร่งด่วน', 'เร่งด่วน'),
        
    ]
    history = HistoricalRecords()
    request_id = models.CharField(max_length=10, blank=True, unique=True,) 
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    sub_item = models.CharField(max_length=100, blank=True)
    detail = models.TextField(max_length=100)
    department = models.CharField(max_length=100)
    device_code = models.CharField(max_length=100, blank=True)
    unknown_device = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='pending')
    status_user = models.CharField(max_length=20, choices=STATUS_CHOICES1)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_staff = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_repairs')
    completed_at = models.DateTimeField(null=True, blank=True )
    in_progress_at = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_repairs')
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    repairclaim_at = models.DateTimeField(null=True, blank=True)
    remark = models.TextField(blank=True)
    asset_number = models.CharField(max_length=255, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.request_id:
            with transaction.atomic():
                last = RepairRequest.objects.select_for_update().order_by('-id').first()
                next_id = 1 if not last else last.id + 1
            self.request_id = f"RQ{next_id:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.request_id} | {self.department} | {self.category} | {self.status}"
    
    def duration(self):
        if self.completed_at and self.in_progress_at:
            return self.completed_at - self.in_progress_at
        return None
    
    def claim_duration(self):
        if self.repairclaim_at and self.completed_at:
            return self.completed_at - self.repairclaim_at
        return None
    class Meta:
        ordering = ['-created_at']
        verbose_name = "รายการแจ้งซ่อม"
        verbose_name_plural = "รายการแจ้งซ่อมทั้งหมด"

class OpdUser(models.Model):
    loginname = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.loginname} - {self.name}'

