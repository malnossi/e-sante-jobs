from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie

from .views import WebUiView

urlpatterns = [
    path('', ensure_csrf_cookie(WebUiView.as_view()),name="index")
]