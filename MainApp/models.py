from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.



class UploadedCSVFile(models.Model):
    file_name = models.FileField(upload_to="csvs", verbose_name=_("File Name"))
    timeframe = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
    jsonfile = models.FileField(upload_to="jsonfiles", verbose_name=_("Download JSON File"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.file_name}"

    class Meta:
        verbose_name = "Uploaded CSV File"
        verbose_name_plural = "Uploaded CSV Files"
        db_table = "uploadedcsvfiles"


class Candle(models.Model):
    name = models.CharField(max_length=150, blank=True)
    date = models.DateField()
    time = models.TimeField()
    open = models.FloatField(blank=True)
    high = models.FloatField(blank=True)
    low = models.FloatField(blank=True)
    close = models.FloatField(blank=True)
    volume = models.PositiveBigIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Candle"
        verbose_name_plural = "Candles"
        db_table = "candles"