from django.shortcuts import render,redirect#,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Participant
from questions.models import Question
from .forms import LoginForm,RegisterForm

# Create your views here.

def index2(request):
    logform = LoginForm()
    regform = RegisterForm()
    return render(request,"index2.html", {'lform' : logform, 'rform' : regform })

def index(request,lout):
    return render(request,"index.html",{'lout' : lout})
    
def login_view(request):
    active = -1
    auth = -1
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/users/dashboard')
                else:
                    form = LoginForm()
                    active = 0
            else:
                form = LoginForm()
                auth = 0
    else:
        form = LoginForm()
    return render(request,"login.html",{'form' : form, 'active' : active, 'auth' : auth})
    
def register(request):
    success = 0
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['pwdcnf'])
            new_user.save()
            p = Participant()
            p.user = new_user
            p.level = 0
            p.points = 0.0
            p.status = 1
            p.rank = Participant.objects.count() + 1
            p.save()
            form = RegisterForm()
            success = 1
    else:
        form = RegisterForm()
    return render(request,"register.html",{'form' : form, 'success' : success})
    
def dashboard(request):
    if request.user.is_authenticated():
        p = Participant.objects.get(user=request.user)
        if p.status == 1:
            #qs = Participant.objects.all()
            #for i,item in enumerate(qs):
             #   if item == p:
              #      rank = i + 1
               #     break
            if p.level != 4:
                slug = Question.objects.get(level = p.level).slug
            else:
                slug = 'none'
            return render(request,"dashboard.html",{'p' : p, 'slug' : slug})

def leaderboard(request):
    p = Participant.objects.all()
    c = Participant.objects.count()
    paginator = Paginator(p, 10) 
    page = request.GET.get('page')
    try:
        pg = paginator.page(page)
    except PageNotAnInteger:
        pg = paginator.page(1)
    except EmptyPage:
        pg = paginator.page(paginator.num_pages)
        
    nos = [i+1 for i in range(pg.paginator.num_pages)]
    
    return render(request,"leaderboard.html",{ 'parts' : p , 'count' : c, 'page' : pg, 'nos' : nos})
                
def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect(reverse('index', kwargs = { 'lout' : 2}))
        #return render(request,"logout.html")
    