from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ContactMessage, BlogPost

def portfolio_home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, "Transmission received successfully! Main jald aapse rabta karunga.")
            return redirect('portfolio_home')
            
    return render(request, 'core/index.html')

def blog_list_view(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'core/blog_list.html', {'posts': posts})

def blog_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'core/blog_detail.html', {'post': post})