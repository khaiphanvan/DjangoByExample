from django.urls import path
from . import views

app_name='images'

urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),
    # login / logout urls
    # path('', views.user_login, name='index'),
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:tilte>', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
]