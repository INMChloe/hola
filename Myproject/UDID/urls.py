from . import views
from django.urls import path

app_name="UDID"

urlpatterns = [
    
    path('', views.Chloe, name="Njeri"),

]