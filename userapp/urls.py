from django.urls import path

from userapp import views

app_name = 'userapp'

urlpatterns = [
    path('login/', views.UserApiView.as_view(), name='login'),
    path('', views.UserView.as_view(), name='user_page'),
]