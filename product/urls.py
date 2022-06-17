from django.urls import path

from product import views

urlpatterns = [
    path('events/', views.ProductApiView.as_view(), name="event_CRUD")
]
