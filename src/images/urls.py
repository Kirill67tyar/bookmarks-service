from django.urls import path
from images.views import (create_view, detail_view,
                          my_detail_view, like_view,
                          experiment, list_view,
                          set_likes)

app_name = 'images'


urlpatterns = [
    path('create/', create_view, name='create'),

    # для обработчика из книги
    path('detail/<int:id>/<slug:slug>/', detail_view, name='detail'),
    # OR
    # для моего обработчика
    # path('detail/<int:id>/<slug:slug>/', my_detail_view, name='detail'),

    path('list/', list_view, name='list'),
    path('like/', like_view, name='like'),

    path('set-likes/', set_likes, name='set_likes'),


    # --------------------------------------------
    path('experiment/', experiment, name='experiment'),

]
