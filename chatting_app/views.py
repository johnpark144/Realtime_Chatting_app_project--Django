
from email import message
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from django.utils import timezone
from .models import Chatting
from .forms import UserForm

@login_required(login_url='chatting_app:login')
def chatting_room(request):  
    messages = Chatting.objects.order_by('create_date') 
    context = {'messages': messages}   
    return render(request, 'chatting.html', context)

@login_required(login_url='chatting_app:login')
def send(request):
    messages = Chatting(username = request.user, content=request.POST.get('text'), create_date=timezone.now())
    messages.save()
    return redirect(resolve_url('chatting_app:chatting_room')+'#last_msg')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증 (사용자명과 비밀번호가 정확한지 검증)
            login(request, user)    # 로그인 시키기
            return redirect('chatting_app:chatting_room')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='common:login')
def message_delete(request, message_id):
    message = get_object_or_404(Chatting, pk=message_id)
    if request.user.username != message.username :
        return redirect(resolve_url('chatting_app:chatting_room')+'#last_msg')
    message.content = "Deleted message"
    message.save()
    return redirect(resolve_url('chatting_app:chatting_room')+'#last_msg')
   
