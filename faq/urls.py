from . import views
from django.views import View
from django.urls import path

urlpatterns = [
     path("faq", views.FaqList, name="faq"),
]
