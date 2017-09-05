from django.conf.urls import url
from . import views

app_name = 'film'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^dysk/$', views.dysk_view, name='dysk-films'),

    url(r'^netflix/$', views.netflix_view, name='netflix-films'),

    url(r'^add/$', views.FilmCreate.as_view(), name='film-add'),

    url(r'^update/(?P<pk>[0-9]+)/$', views.FilmUpdate.as_view(), name='film-update'),

    url(r'^delete/(?P<pk>[0-9]+)/$', views.FilmDelete.as_view(), name='film-delete'),

    url(r'^all/filter/gatunek/(?P<genre>[a-zA-Z ]+)/$', views.filtering_gatunek_all, name='film-filter-all'),

    url(r'^dysk/filter/gatunek/(?P<genre>[a-zA-Z ]+)/$', views.filtering_gatunek_dysk, name='film-filter-dysk'),

    url(r'^netflix/filter/gatunek/(?P<genre>[a-zA-Z ]+)/$', views.filtering_gatunek_netflix, name='film-filter-netflix'),

    url(r'^szukaj/all/$', views.searching_all, name='film-search-all'),

    url(r'^szukaj/dysk/$', views.searching_dysk, name='film-search-dysk'),

    url(r'^szukaj/netflix/$', views.searching_netflix, name='film-search-netflix'),

    url(r'^all/filter/nota/$', views.filtering_nota_all, name='film-filter-all-nota'),

    url(r'^dysk/filter/nota/$', views.filtering_nota_dysk, name='film-filter-dysk-nota'),

    url(r'^netflix/filter/nota/$', views.filtering_gatunek_netflix, name='film-filter-netflix-nota'),

    url(r'^wylosuj/$', views.drawing, name='film-drawing'),
]