from django.urls import path 
from .views import login,logout,register,profile
from django.conf import settings


app_name = 'accounts'

urlpatterns = [
    path('login/',login,name="login"),
    path('register/',register,name="register"),
    path('logout/',logout,name="logout"),
    path('profile/',profile,name="profile")

]
# if settings.DEBUG :
#     urlpatterns+=static(settings.MEDIA_URL,document_root= settings.MEDIA_URL) 

 