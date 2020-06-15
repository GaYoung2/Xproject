from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Account

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        student_num = request.POST.get('student_num', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {} 
        if not (student_num and username and password and re_password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            account = Account(student_num = student_num, username = username, password = make_password(password))
            account.save()
        return render(request, 'register.html', res_data)

def login(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'login.html')

    elif request.method == "POST":
        login_student_num = request.POST.get('student_num', None)
        login_password = request.POST.get('password', None)

        if not (login_student_num and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else: 
            account = Account.objects.get(student_num=login_student_num) 
            if check_password(login_password, account.password):
                request.session['user'] = account.id
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'login.html', response_data)

def home(request):
    account_id = request.session.get('user')
    if account_id:
        account_info = Account.objects.get(pk = account_id)
        return HttpResponse(account_info.username)

    return HttpResponse('로그인을 해주세요.')

def logout(request):
    request.session.pop('user')
    return redirect('/')