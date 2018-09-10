from django.conf.urls import include, url
from . import views

movies_routes = [
    url(r'^allMovies$', views.movies_summary),
    url(r'^new$', views.new_movie),
    url(r'^(?P<movie_id>[a-zA-Z0-9]+)/$', views.movie_details),
    url(r'^.*$', views.movies_summary)
]

auth_routes = [
    url(r'^csrf$', views.send_csrf),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^username-exists/$', views.username_exists)
]

user_data_routes = [
    url(r'^get-data/$', views.get_user_data),
    url(r'^update/$', views.update_data),
    url(r'^update-password/$', views.update_password),
    url(r'^delete/$', views.delete_account)
]

urlpatterns = [
    url(r'^movie/', include(movies_routes)),
    url(r'^auth/', include(auth_routes)),
    url(r'^user/', include(user_data_routes))
]
