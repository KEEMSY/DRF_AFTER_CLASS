from django.urls import path

from assignmnet import views
from assignmnet.views import TestView

app_name = 'assignment'

urlpatterns = [
    path('test/', views.TestView.as_view(), name='test')
]