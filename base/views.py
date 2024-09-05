from django.shortcuts import render, redirect, HttpResponse
from .models import Task,HistoryModel,CompletedModel
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import Contactus
from .models import ContactModel
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

@login_required(login_url='login_')
def home(request):
    a=Task.objects.filter(host=request.user)
    all=[]
    if request.method == 'GET':
        if 'q' in request.GET:
            q=request.GET['q']
            print(q)
            all=Task.objects.filter((Q(title__icontains=q) & Q(host=request.user)) | (Q(desc__icontains=q) & Q(host=request.user)))
            print(len(all))
            if len(all)==0:
                all=[{'id':0,'title':'No Record Found','desc':'No Record Found'}]
        else:
            all=Task.objects.filter(host=request.user)
    return render(request,'home.html',context={'a':all})

@login_required(login_url='login_')
def addtask(request):
    if request.method == 'POST':
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        Task.objects.create(title=title,desc=desc,host=request.user)
        return redirect('home')
    return render(request,'addtask.html')

def details(request,id):
    a=Task.objects.get(id=id)
    return render(request,'details.html',{'a':a})

def edit(request,id):
    a=Task.objects.get(id=id)
    print(a)
    if request.method == 'POST':
        title=request.POST['title']
        desc=request.POST['desc']
        a.title=title
        a.desc=desc
        a.save()
        return redirect('home')
    return render(request,'addtask.html',{'a':a})

def delete(request,id):
    a=Task.objects.get(id=id)
    if request.method =='POST':
        HistoryModel.objects.create(id=id,title=a.title,desc=a.desc,host=request.user)
        a.delete()
        return redirect('home')
    return render(request,'delete.html',{'a':a})
        
def history(request):
    h=HistoryModel.objects.filter(host=request.user)
    return render(request,'history.html',context={'h':h})

def restore(request,id):
    h=HistoryModel.objects.get(id=id)
    Task.objects.create(id=id,title=h.title,desc=h.desc,host=request.user)
    h.delete()
    return redirect('home')

def restoreall(request):
    h=HistoryModel.objects.filter(host=request.user)
    for i in h:
        Task.objects.create(id=i.id,title=i.title,desc=i.desc,host=request.user)
        i.delete()
    return redirect('home')

def historydelete(request,id):
    d=HistoryModel.objects.get(id=id)
    d.delete()
    return redirect('history')

def clearall(request):
    c=HistoryModel.objects.filter(host=request.user)
    c.delete()
    return redirect('history')

def complete(request,id):
    a=Task.objects.get(id=id)
    CompletedModel.objects.create(id=id,title=a.title,desc=a.desc,host=request.user)
    a.delete()
    return redirect('completed')

def completed(request):
    c=CompletedModel.objects.filter(host=request.user)
    return render(request,'completed.html',context={'c':c})

def completedelete(request,id):
    d=CompletedModel.objects.get(id=id)
    d.delete()
    return redirect('completed')

def completeclearall(request):
    c=CompletedModel.objects.filter(host=request.user)
    c.delete()
    return redirect('completed')

def about(request):
    about={
        'desc':'''In our team, effective task management is the cornerstone of our project success. We understand that every project, regardless of its scale, requires a well-organized approach to ensure timely and quality outcomes. Our task management strategy is designed to foster collaboration, maintain focus, and achieve our goals efficiently.

Core Principles:

Clarity and Organization: We believe in breaking down complex projects into manageable tasks. Each task is clearly defined with specific objectives, deadlines, and assigned responsibilities, ensuring that every team member knows what is expected.

Prioritization: Not all tasks are created equal. We prioritize tasks based on urgency and importance, allowing us to focus our efforts where they are needed most. This approach helps in avoiding bottlenecks and ensures that critical milestones are met on time.'''
    }
    return render(request,'about.html',context={'about':about})

def contactus(request):
    context={'Contactus':Contactus}
    if request.method=='POST': 
        f=Contactus(request.POST)
        if f.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            subject=request.POST['subject']
            message=request.POST['message']
            print(name,email,subject,message)
            ContactModel.objects.create(name=name,email=email,subject=subject,message=message,host=request.user)
            return redirect('contactsuccess')
    return render(request,'contactus.html',context)


def contactsuccess(request):
    return render(request,'contactsuccess.html')

def profile(request):
    return render(request,'profile.html')

def updateprofile(request, id):
    u=User.objects.get(id=id)
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        u.first_name=first_name
        u.last_name=last_name
        u.email=email
        u.username=username
        u.save()
        return redirect('profile')
    return render(request,'updateprofile.html',{'u':u})

def deleteprofile(request, id):
    u=User.objects.get(id=id)
    u.delete()
    logout(request)
    return redirect('login_')

def changepassword(request, id):
    u=User.objects.get(id=id)
    invalid=''
    if request.method=='POST':
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        if u.password==current_password:
            u.password=new_password
            u.save()
            logout(request)
            return redirect('login_')
        else:
            invalid='Invalid current password'
    return render(request,'changepassword.html',{'u':u,'invalid':invalid})