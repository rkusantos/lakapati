from django.urls import path
from django.conf.urls import *
from . import views

app_name = 'function'

urlpatterns = [
    path('input_farm/', views.InputFarmView.as_view(template_name="functions/input_farm.html"), name='input_farm'),
    path('check_farm/', views.CheckFarmView.as_view(template_name="functions/check_farm.html"), name='check_farm'),
    path('analysis/', views.AnalysisView.as_view(template_name="functions/analysis.html"), name='analysis'),
]