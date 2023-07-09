from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Images


@login_required
def image_create(request):
    print("shrasta")
    # form = ImageCreateForm()
    form = ImageCreateForm(data=request.GET)

    if request.method == 'POST':
        print("\n\nshrasta\n\n")
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            print('rai')
            # form data is valid
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assign current user to the item
            new_image.user = request.user
            new_image.save()

            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_image.get_absolute_url())

        # else:
            # build form with data provided by the bookmarklet via GET
            # form = ImageCreateForm(data=request.GET)
            # if form.is_valid():
            #     title = form.cleaned_data.get('title')
            #     form.initial['title'] = title
            # print('\n\n Else statement \n\n')
    return render(request, 'images/image/create.html',{'form':form})



def image_detail(request, id, slug):
    image = get_object_or_404(Images, id=id, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images','image': image})