from django.urls import path

from . import views
from core.views import about


urlpatterns= [
    path('search/', views.search, name='search'),
    path('about/', about, name='about'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
] 