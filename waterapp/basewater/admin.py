from django.contrib import admin
from .models import User, Report, WaterQuality
# Register your models here.
admin.site.register(User)
admin.site.register(Report)
admin.site.register(WaterQuality)