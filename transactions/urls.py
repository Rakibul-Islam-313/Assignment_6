from django.urls import path
from .views import DepositFormView
urlpatterns = [
    path('deposit/',DepositFormView.as_view(), name='deposit_page'),
]
