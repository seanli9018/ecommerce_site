from django.urls import path
from .views import LoginView, CaptchaView, ResigterView, StaffLoginView

app_name = 'ecauth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('captcha/', CaptchaView.as_view(), name='captcha'),
    path('register/', ResigterView.as_view(), name='register'),
    path('cms/login/', StaffLoginView.as_view(), name='cms_login'),
]