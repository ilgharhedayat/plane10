from django.urls import path

from .views import (
    UserLoginView,
    UserLogoutView,
    UserRegisterVerifyCodeView,
    UserRegisterView,
)

app_name = "accounts"
urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("verify/", UserRegisterVerifyCodeView.as_view(), name="verify"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
