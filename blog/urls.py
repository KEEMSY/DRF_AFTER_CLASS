from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.ArticleApiView.as_view(), name='article_C'),
    path('test-create/', views.TestArticleApiView.as_view(), name='article_C'),
]