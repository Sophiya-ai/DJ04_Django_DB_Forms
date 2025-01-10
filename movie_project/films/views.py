from django.shortcuts import render, redirect
from .models import New_film  #импортируем класс
#from .forms import New_postForm

# Create your views here.
def display_filmsdescription(request):
    return render(request, 'films/watchDBfilms.html')
    #films = New_film.objects.all()   #Создаём переменную для получения всех записей
   # return render(request,'films/watchDBfilms.html', {'films' : films})
    #Прописываем словарь для передачи информации в html-шаблон

def add_films(request):
    return render(request, 'films/add_films.html')
    # error = ''
    # if request.method == 'POST':
    #     form = New_filmForm(request.POST) #сохраняем всю информацию от пользователя
    #     if form.is_valid():
    #         form.save()
    #         return redirect('displayFilm')
    #     else:
    #         error = "Данные заполнены некорректно"
    # form = New_filmForm()
    # return render(request, 'films/add_films.html', {'form' : form, 'errors': error})