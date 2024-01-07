from django.urls import path
from .views import SignUpFormView,LoginFormView,LogoutFormView
from . import views
urlpatterns = [
    path('sign_up/',SignUpFormView.as_view(), name = 'sign_up_page'),
    path('login/',LoginFormView.as_view(), name = 'login_page'),
    path('logout/',LogoutFormView.as_view(), name = 'logout_page'),
    
    path('profile/',views.ProfileView, name = 'profile_page'),

]
