from django import forms
from .models import UploadedCSVFile, Candle



class UploadedCSVFileForm(forms.ModelForm):
    class Meta:
        model = UploadedCSVFile
        fields = ('file_name', 'timeframe',)