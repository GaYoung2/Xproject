from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    form = SignUpForm(request.POST)
    print(form)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'form':form})