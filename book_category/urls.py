from django.urls import path
from .views import categoryView
urlpatterns = [
    path('category/', categoryView.as_view())
]