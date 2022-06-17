from django.urls import path

from product import views

app_name = "product_app"

urlpatterns = [
    path('events/', views.ProductApiView.as_view(), name="event_CRUD")
]
