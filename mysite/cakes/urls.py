from django.urls import path

from . import views

urlpatterns = [
    path('cakes/', views.cakes, name='cakes'),
    path('cake/<int:cake_id>/', views.cake, name='cake'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('sample/<int:sample_id>/', views.sample, name='sample'),
    path('fillings/', views.fillings, name='fillings'),
    path('about/', views.about_us, name='about_us'),
    path('order/', views.order, name='order'),
    path('reviews/', views.reviews, name='reviews'),


]
