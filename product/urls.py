from django.urls import path

from product import views

app_name = "product_app"

urlpatterns = [
    path('events/', views.EventApiView.as_view(), name="event_CR"),
    path('events/<obj_id>/', views.EventApiView.as_view(), name="event_UD"),

    path('', views.ProductApiView.as_view(), name="product_CR"),
    path('<obj_id>/', views.ProductApiView.as_view(), name="product_UD"),

    path('reviews/', views.ReviewApiView.as_view(), name="review_CR"),

]
