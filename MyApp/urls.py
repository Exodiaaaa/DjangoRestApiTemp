from . import views,api
from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data', views.dht11, name='Data'),
    path('charts/', views.EditorChartView.as_view(), name='CH'),
    path('csv/', views.exp_csv, name='exp-csv'),
    path('api/list', api.Dlist, name='DHT11List'),
    path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
]
