from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.utils import timezone
from .models import Chatting
from .forms import UserForm

@login_required(login_url='chatting_app:login')
def chatting_room(request):  
    messages = Chatting.objects.order_by('create_date')     # New message has to come out on very bottom.
    context = {'messages': messages}   
    return render(request, 'chatting.html', context)

@login_required(login_url='chatting_app:login')
def send(request):
    messages = Chatting(username = request.user, content=request.POST.get('text'), create_date=timezone.now())
    messages.save()
    return redirect(resolve_url('chatting_app:chatting_room')+'#last_msg') # whenever messages sent, last one is anchor to redirect

def signup(request):
    if request.method == "POST":    # When someone complete the sign-up.
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # User authentication (to verify username and password)
            login(request, user)    # Make them loged in
            return redirect('chatting_app:chatting_room')
    else:   # When someone start the sign-up.
        form = UserForm()
    return render(request, 'signup.html', {'form': form}) # Use the form created in signup templete.

@login_required(login_url='common:login')
def message_delete(request, message_id):
    message = get_object_or_404(Chatting, pk=message_id)    # To check if the message with its id exist 
    if request.user.username != message.username :  # To prevent from other user's deleting messages in not proper way.
        return redirect(resolve_url('chatting_app:chatting_room')+'#last_msg')
    message.content = "Deleted message"
    message.save()
    return redirect(resolve_url('chatting_app:chatting_room')+'#last_msg')
   
