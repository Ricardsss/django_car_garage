from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from .views import AuthView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "garage/",
        include("garage.urls"),
    ),
    path("accounts/register/", AuthView.custom_register, name="register"),
    path("accounts/login/", AuthView.custom_login, name="login"),
    path("accounts/logout/", AuthView.custom_logout, name="logout"),
    path("", RedirectView.as_view(url="garage/", permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
