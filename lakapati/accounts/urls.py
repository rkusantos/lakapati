from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"),name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="logout"),
]