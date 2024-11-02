from django.shortcuts import render, redirect
from .models import Message

def home(request):
    messages = Message.objects.all().order_by('-created_at')[:1]  # Fetch the latest message
    return render(request, 'home.html', {'messages': messages})

def form_view(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(content=content)
        return redirect('home')
    return render(request, 'form.html')