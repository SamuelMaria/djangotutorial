from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='/polls/', permanent=False)),
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()
