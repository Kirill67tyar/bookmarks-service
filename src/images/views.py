from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from images.forms import ImageCreateModelForm



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


# bookmarklet_launcher.js