from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addrecipie',views.addrecipie),
    path('viewrecipie',views.viewrecipie),
    path('searchrecipie',views.searchrecipie),
    
]

