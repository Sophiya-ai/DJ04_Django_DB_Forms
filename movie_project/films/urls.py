from django.urls import path
from . import views

# Для работы со статическим файлами подключаем:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.add_films, name='addFilm'),
    path('watchDBfilms/', views.display_filmsdescription, name='displayFilm'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Для работы со статическим файлами, прописываем их подключение и использование