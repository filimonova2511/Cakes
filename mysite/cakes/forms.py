from django import forms
from .models import Review, Cake, Product, Filling


class ReviewForm(forms.Form):
    name = forms.CharField(label='Имя')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Ваш отзыв')


class OrderForm(forms.Form):
    name = forms.CharField(label='Имя')
    date = forms.DateField(input_formats=['%d.%m.%Y'], label='Дата мероприятия')
    weight = forms.IntegerField(label='Вес торта')
    cake = forms.ModelChoiceField(queryset=Cake.objects.all(), label='Категория')
    products = forms.ModelChoiceField(queryset=Product.objects.all(), label='Событие')
    filling = forms.ModelChoiceField(queryset=Filling.objects.all(), label='Начинка')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Примечание')







