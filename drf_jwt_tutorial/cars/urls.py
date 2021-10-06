from django.conf.urls import url
from django.urls import path
from cars import views

urlpatterns = [
    path('all/', views.get_all_cars),
    path('', views.user_cars),
]