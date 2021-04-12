from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse
from accounts.forms import LoginForm



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
                        return HttpResponse('Authenticated was successfully')
                    else:
                        return HttpResponse('User is not active')
                else:
                    return HttpResponse('Invalid login/password')
        else:
            form = LoginForm()
            print(f'\n\nUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n'
              f'LoginForm().is_valid() - {form}'
              f'\n\n\nUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n\n\n')
        return render(request, 'accounts/login.html', {'form': form,})
    else:
        return HttpResponse('You already authenticated')

