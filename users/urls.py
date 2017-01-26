from django.conf.urls import url
from .views import login_view,register,logout_view,dashboard,leaderboard
 
urlpatterns = [ 
    url(r'^login$',login_view,name='login'),
    url(r'^register$',register,name='register'),
    url(r'^logout$',logout_view,name='logout'),
    url(r'^dashboard$',dashboard,name='dashboard'),
    url(r'^leaderboard$',leaderboard,name='leaderboard'),
    ]