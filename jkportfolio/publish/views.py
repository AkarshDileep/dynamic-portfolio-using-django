from django.shortcuts import render
from .models import published 
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login.html')
def papers(request):
    if request.POST:
        title = request.POST.get('title')
        image = request.POST.get('image')
        content = request.POST.get('content')
        type=request.POST.get('type')
        summary=request.POST.get('summary')
        p1=published(title=title,image=image,content=content,type=type,summary=summary)
        p1.save()
    return render(request,'publish.html')
def profile(request):
    data=published.objects.all()
    papers={'papers':data}
    return render(request,'index.html',papers)
def detailed(request,pk):
    publishedlist=published.objects.get(pk=pk)
    content={'publish':publishedlist,}
    return render(request,'view.html',content)

from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect

def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('jk/')
        
    return render(request, 'login.html')
