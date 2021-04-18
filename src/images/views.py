from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy

from images.forms import ImageCreateModelForm
from images.models import Image


@login_required
def create_view(request):
    if request.method == 'POST':
        form = ImageCreateModelForm(request.POST)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image saving was successfully')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateModelForm(data=request.GET)

    context = {
        'section': 'images',
        'form': form,
    }
    return render(request, 'images/image/create.html', context=context)


# обработчик из книги. Делает 9 SQL запросов
def detail_view(request, id, slug):
    image = get_object_or_404(Image, pk=id, slug=slug)
    context = {
        'image': image,
    }
    return render(request, 'images/image/detail.html', context=context)


# мой обработчик. Вместо 9 SQL запросов делает 5 SQL запросов
# но как видно реализован более сложным (рефакторинг кода, ревью сложнее роддерживать)
# плюс здесь нельзя использовать get_absolute_url()
def my_detail_view(request, id, slug):
    image_qs = Image.objects.filter(pk=id, slug=slug).annotate(cnt=Count('users_like'))
    image = image_qs.values('title', 'image', 'description', 'cnt').first()
    image['image'] = '/media/' + image['image']
    users_like = image_qs.first().users_like.all().values('username', 'profile__photo')
    for user in users_like:
        if user['profile__photo']:
            user['profile__photo'] = '/media/' + user['profile__photo']
    context = {
        'image': image,
        'users_like': users_like,
    }
    return render(request, 'images/image/my_detail.html', context=context)


# some-picture
# bookmarklet_launcher.js