from .models import New_film
from django.forms import ModelForm, TextInput,Textarea

class New_filmForm(ModelForm):
    class Meta:
        model = New_film
        fields = ['title', 'short_description', 'feedback']
        widgets = {
            'title' : TextInput(attrs={'class' : "form-control", 'placeholder':"Введите название фильма"}),
            'short_description' : TextInput(attrs={'class' : "form-control", 'placeholder':"Введите краткое описание фильма"}),
            'feedback' : Textarea(attrs={'class' : "form-control", 'placeholder':"Введите отзыв на фильм"}),
        }