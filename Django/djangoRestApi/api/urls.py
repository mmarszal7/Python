from django.conf.urls import url
from . import views

movies_routes = [
    url(r'^get-all$', views.movies_summary, name='movies summary'),
    url(r'^movie/new$', views.new_movie, name='new movie'),
    url(r'^movie/(?P<movie_id>[a-zA-Z0-9]+)/$', views.movie_details, name='movie details'),
]

auth_routes = [
    url(r'^auth/csrf$', views.send_csrf, name='send csrf token'),
    url(r'^auth/login/$', views.login, name='login'),
    url(r'^auth/register/$', views.register, name='register'),
    url(r'^auth/username-exists/$', views.username_exists, name='check unique username'),
]

user_data_routes = [
    url(r'^user/get-data/$', views.get_user_data, name='get user data'),
    url(r'^user/update/$', views.update_data, name='update user data'),
    url(r'^user/update-password/$', views.update_password, name='update user password'),
    url(r'^user/delete/$', views.delete_account, name='delete user account')
]

urlpatterns = movies_routes + auth_routes + user_data_routes

