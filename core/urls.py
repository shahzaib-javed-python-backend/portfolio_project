from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_home, name='portfolio_home'),
    path('blog/', views.blog_list_view, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail_view, name='blog_detail'),
]