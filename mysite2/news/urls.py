from django.urls import path
from. import views

app_name = 'news'

urlpatterns = [
    path('all/',views.all, name='all'),
    path('trending/',views.trending, name='trending'),
    path('sport/', views.sport, name='sport'),
    path('politics/', views.politics, name='politics'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('healty/', views.healty, name='healty'),
    path('entartaiment/', views.entartaiment, name='entartaiment'),
    path('isi/<int:id>',views.isi, name='isi'),

]
