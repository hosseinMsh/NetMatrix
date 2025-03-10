from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser ):
    is_admin = models.BooleanField(default=False)  # آیا کاربر ادمین است یا خیر
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # شماره تلفن
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین به‌روزرسانی
    level = models.IntegerField(default=1)  # سطح دسترسی کاربر (1: کاربر عادی، 2: مسئول فنی، 3: مسئول حقوقی)

    def __str__(self):
        return self.username

class VirtualMachine(models.Model):
    name = models.CharField(max_length=255)  # نام ماشین مجازی
    technical_responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='technical_responsible')
    legal_responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='legal_responsible')
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین به‌روزرسانی

    def __str__(self):
        return self.name

class Server(models.Model):
    name = models.CharField(max_length=255)  # نام سرور
    internal_ip = models.GenericIPAddressField()  # IP داخلی
    public_ip = models.GenericIPAddressField()  # IP عمومی
    virtual_machine = models.ForeignKey(VirtualMachine, on_delete=models.CASCADE, related_name='servers')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_servers')  # مالک سرور
    open_ports = models.CharField(max_length=255, blank=True, null=True)  # پورت‌های باز
    access_status = models.BooleanField(default=True)  # وضعیت دسترسی
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین به‌روزرسانی

    def __str__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=255)  # نام دامنه
    ssl_expiration_date = models.DateField()  # تاریخ انقضای SSL
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='domains')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_domains')  # مالک دامنه
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین به‌روزرسانی

    def __str__(self):
        return self.name

class History(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='history_records')  # سرور مرتبط
    status = models.BooleanField(default=True)  # وضعیت سرور (فعال یا غیرفعال)
    timestamp = models.DateTimeField(auto_now_add=True)  # زمان ثبت تاریخچه
    notes = models.TextField(blank=True, null=True)  # یادداشت‌ها یا توضیحات

    def __str__(self):
        return f"History for {self.server.name} at {self.timestamp}"