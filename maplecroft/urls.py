from django.urls import path

from maplecroft.views import Index


urlpatterns = [
    path('', Index.as_view()),
]