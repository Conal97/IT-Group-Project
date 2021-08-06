from django.urls import path, include
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
    path('search', views.search, name='search'),
    path('search_munros', views.search_munros, name='search_munros'),
    path('photo_gallery/', views.photo_gallery, name='photo_gallery'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('search_munros/', views.search_munros, name='search_munros'),
    path('munros/<slug:munro_name_slug>/', views.show_munro, name='show_munro'),
    path('goto/', views.goto_url, name='goto'),
    path('like_area/', views.LikeAreaView.as_view(), name='like_area'),
    path('like_munro/', views.LikeMunroView.as_view(), name='like_munro'),
    path('user_likes_area/', views.UserLikesArea.as_view(), name='user_likes_area'),
    path('post_report/', views.hike_report, name='post_report'),
]