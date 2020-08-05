from django.urls import path
from .views import show,detail,like,update,delete

app_name = 'videos'

urlpatterns = [
    path('',show,name="show"),
    path('detail/<int:id>/',detail,name="detail"),
    path('like/<int:id>/',like,name="like"),
    path('update/<int:id>/',update,name="update"),
    path('delete/<int:id>/',delete,name="delete"),

]
