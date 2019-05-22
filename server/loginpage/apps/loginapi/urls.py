from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
]

 # path('<int:user_id>',views.show),
