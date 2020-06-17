from django.shortcuts import render, redirect
from django.contrib.auth import views, models, login, authenticate

from .forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
    
        if form.is_valid():
            new_user = models.User.objects.create_user(**form.cleaned_data)
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, new_user)
        
        return redirect('index')

    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})