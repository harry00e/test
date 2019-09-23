from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import FileResponse
from os import listdir
from os.path import isfile, join
import random

USER_DICT={"username":['test'],"test":"test"}


# Create your views here.

def login(request):
    user_list=[] #{'user':'abc','pwd':'1234'}]
    message = ""
    logout = False
    register = None
    status='info'
    if request.method=="POST":
        username= request.POST.get("username",None)
        password= request.POST.get("password",None)
        register = request.POST.get("register",None)
        # print(register)
        temp={"user":username,"pwd":password,"register":register}
        user_list.append(temp)
        if 'username' in request.session :
            # print(request.session['username'])
            if request.session['username'] in USER_DICT.keys():
                message = username + " 已登入！"
                logout = True

        if register == "on":
            if not username in USER_DICT.keys():
                USER_DICT[username]=password
                message= '帳號建立成功!! 請重新登入...'
            else:
                message = '帳號已被使用!! 請重新註冊(Register)新帳號.'
                # print(message)
        elif username in USER_DICT.keys():
            if USER_DICT[username]==password:
                # request.session['username'] = username  # 儲存Session
                request.session['username'] = username
                # message = username  + " 您好，登入成功！"
                USER_DICT['username'].append(username)
                logout=True
                return redirect('/player/')
                # return HttpResponse(message)
            else:
                message = username + " 登入失敗!! "
                status='error'
        else:
            message = username + " 登入失敗!! "
            status='error'
    else:
        if 'username' in request.session:
            # print(request.session['username'] )
            if request.session['username'] in USER_DICT.keys():
                message = request.session['username'] + " 已登入！"
                logout=True
    return render(request, 'login.html',{'message': message ,'logout': logout,'status':status})

def logout(request):
    status=True
    message=""
    if 'username' in request.session:
        message=request.session['username'] + ' 您已登出!'
        if request.session['username'] in USER_DICT['username']:
            USER_DICT['username'].remove(request.session['username'])
        del request.session['username']	#刪除Session
        status=False
    return redirect("/login/")
    # return render(request, 'login.html',locals())

def player(request):
    if 'username' not in request.session:
        return redirect("/login/")
    else:
        return render(request,"player.html",locals())

def music(request):
    if 'username' not in request.session:
        return redirect("/login/")
    false=0
    musicFiles = [{'Name':f, "IsDir":false} for f in listdir('./music/') if isfile(join('./music/', f))]
    random.shuffle(musicFiles)
    return HttpResponse(str(musicFiles[0:10]))
    # return render(requests,"player.html",locals())

def playmusic(request):
    if 'username' not in request.session:
        return redirect("/login/")
    filename=request.GET.get('file', '')
    fullname='./music/'+filename
    response = FileResponse(open(fullname, 'rb'))
    # response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename='+filename
    return response

