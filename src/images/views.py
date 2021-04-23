from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy

from images.forms import ImageCreateModelForm
from images.models import Image
from actions.utils import create_action
from common.decorators import ajax_required

@login_required
def create_view(request):
    if request.method == 'POST':
        form = ImageCreateModelForm(request.POST)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            create_action(request.user, 'Image bookmarked', new_image)
            messages.success(request, 'Image saving was successfully')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateModelForm(data=request.GET)

    context = {
        'section': 'images',
        'form': form,
    }
    return render(request, 'images/image/create.html', context=context)


# обработчик из книги. Делает 9 SQL запросов (с sorl.thumbnail 10 и 9)
def detail_view(request, id, slug):
    image = get_object_or_404(Image, pk=id, slug=slug)
    context = {
        'image': image,
    }
    return render(request, 'images/image/detail.html', context=context)


# мой обработчик. Вместо 9 (с sorl.thumbnail 10 и 9) SQL запросов делает 5 (с sorl.thumbnail 8 и 7) SQL запросов
# но как видно реализован более сложным (рефакторинг кода, ревью сложнее поддерживать)
# плюс здесь нельзя использовать get_absolute_url()
def my_detail_view(request, id, slug):
    image_qs = Image.objects.filter(pk=id, slug=slug).annotate(total_likes=Count('users_like'))
    if image_qs:
        image_object = image_qs.first()
        image = image_qs.values('pk', 'title', 'image', 'description', 'total_likes').first()
        image['image'] = '/media/' + image['image']
        users_like = image_qs.first().users_like.all().values('username', 'profile__photo')
        usernames = image_qs.first().users_like.all().values_list('username', flat=True)
        for user in users_like:
            if user['profile__photo']:
                user['profile__photo'] = '/media/' + user['profile__photo']
        context = {
            'image': image,
            'users_like': users_like,
            'image_object': image_object,
            'usernames': usernames,
        }
        return render(request, 'images/image/my_detail.html', context=context)

# ajax_required - декоратор, который проверяет ajax запрос у нас или нет
# если нет то шлем ошибку 400 bad request
@ajax_required# - 400
@login_required
@require_POST# - 405
def like_view(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(pk=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'ok'})




@login_required
def list_view(request):
    qs = Image.objects.all()#.filter(user=request.user)
    paginator = Paginator(qs, 8)
    num_page = request.GET.get('page')
    try:
        images = paginator.page(num_page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        else:
            images = paginator.page(paginator.num_pages)
    context = {
        'section': 'images',
        'images': images,
    }
    if request.is_ajax():
        template_name = 'images/image/list_ajax.html'
    else:
        template_name = 'images/image/list.html'
    return render(request, template_name=template_name, context=context)



def experiment(request):
    return JsonResponse({'cheking': 'it works'})