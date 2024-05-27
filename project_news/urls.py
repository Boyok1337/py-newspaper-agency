from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from newspaper.views import register, PostSearchView

handler404.handler404 = "newspaper.views.custom_404"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("newspaper.urls")),
    path("register/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("search/", PostSearchView.as_view(), name="posts-search"),
]
