from django.contrib import admin
from .models import UploadedCSVFile, Candle
# Register your models here.




@admin.register(UploadedCSVFile)
class UploadedCSVFileAdmin(admin.ModelAdmin):
    list_display = ["file_name", "timeframe", "active", "created_at", "updated_at"]
    list_display_links = list_display



@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "open", "close", "created_at", "updated_at"]
    list_display_links = list_display