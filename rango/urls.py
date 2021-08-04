from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='login'),
    #path('logout/', views.user_logout, name='logout'),
    path('restricted/', views.restricted, name='restricted'),
    path('areas/', views.area, name='areas'),
    path('area/<slug:area_name_slug>/', views.show_area, name='show_area'),
    path('post-report', views.hike_report, name='hike_report'),
    path('search', views.search, name='search'),
    path('photo_gallery/', views.photo_gallery, name='photo_gallery'),
]