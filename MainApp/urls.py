from django.urls import path
from .views import *

urlpatterns = [
    path('', upload_csvfiles_view, name="upload -csvfiles"),
]