from django.urls import path
from warehouse.views import *

urlpatterns = [
    path('',barcode,name='barcode')
]