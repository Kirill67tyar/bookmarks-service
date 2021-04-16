from django.urls import path
from images.views import create_view

app_name = 'images'


urlpatterns = [
    path('create/', create_view, name='create'),

]
