from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from accounts.forms import LoginForm, RegisterModelForm, ProfileEditModelForm, UserEditModelForm
from accounts.models import Profile

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            print(f'\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
                  f'LoginForm(request.POST) - {form}'
                  f'\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n')
            print(f'\n\n########################################\n'
                  f'request.POST - {request.POST}'
                  f'\n########################################\n\n')
            if form.is_valid():
                print(f'\n\n*************************************\n'
                      f'LoginForm(request.POST).is_valid() - {form}'
                      f'\n\n\n*************************************\n\n\n')
                data = form.cleaned_data
                username = data['username']
                password = data['password']
                user = authenticate(request, username=username, password=password)
                print(f'\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
                      f'authenticate(request, username=username, password=password) - {user}'
                      f'\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n')
                if user:
                    if user.is_active:
                        login(request, user)
                        return redirect(reverse('accounts:dashboard'))
                    else:
                        return HttpResponse('User is not active')
                else:
                    return HttpResponse('Invalid login/password')
        else:
            form = LoginForm()
            print(f'\n\nUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n'
                  f'LoginForm().is_valid() - {form}'
                  f'\n\n\nUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n\n\n')
        return render(request, 'accounts/login.html', {'form': form, })
    else:
        return HttpResponse('You already authenticated')

# как мы сможем попасть на запрашиваемую страницу после атентификации?
# с помощью поля <input type="hidden" name="next" value="{{next}}"/> в html форме login
@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})


def register_view(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password'])
            Profile.objects.create(user=new_user)
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user,})
    else:
        form = RegisterModelForm()
    return render(request, 'accounts/register.html', {'form': form,})

@login_required
def edit_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(f'\n\n)))))))))))))))))))))))))))\n'
                  f'request.POST - {request.POST}'
                  f'\n))))))))))))))))))))))))))))\n\n')
            user_form = UserEditModelForm(instance=request.user, data=request.POST)
            profile_form = ProfileEditModelForm(instance=request.user.profile, data=request.POST, files=request.FILES)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request=request, message='Profile updated successfully')
                return render(request=request, template_name='accounts/edit_done.html', context={})
            else:
                messages.error(request=request, message='Error updating your profile')
        else:
            user_form = UserEditModelForm(instance=request.user)
            profile_form = ProfileEditModelForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request=request, template_name='accounts/edit.html', context=context)
    else:
        return redirect(reverse('accounts:login'))

