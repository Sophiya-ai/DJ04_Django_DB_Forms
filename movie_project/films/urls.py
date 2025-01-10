from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_films, name='addFilm'),
    path('watchDBfilms/', views.display_filmsdescription, name='displayFilm'),
]