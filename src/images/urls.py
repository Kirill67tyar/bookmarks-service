from django.urls import path
from images.views import create_view, detail_view, my_detail_view

app_name = 'images'


urlpatterns = [
    path('create/', create_view, name='create'),

    # для обработчика из книги
    # path('detail/<int:id>/<slug:slug>/', detail_view, name='detail'),
    # OR
    # для моего обработчика
    path('detail/<int:id>/<slug:slug>/', my_detail_view, name='detail'),

]
