from django.urls import path, include
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
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
    path('user_likes_munro/', views.UserLikesMunro.as_view(), name='user_likes_munro'),
    path('post_report/', views.hike_report, name='post_report'),
    path('suggest/', views.AreaSuggestionView.as_view(), name='suggest')
]