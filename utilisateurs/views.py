from django.shortcuts import render
from .forms import UserForm, ProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def acceuil(request):
    return render(request, 'utilisateurs/index.html')


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)   
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and  profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered=True
            return HttpResponseRedirect('login')        

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form = ProfileForm()

    content ={
        'registered':registered,
        'form1':user_form,
        'form2':profile_form,
    }
    return render(request, 'utilisateurs/register.html', content)        
            
def user_login(request):
    if request.method != 'POST':
        return render(request, 'utilisateurs/login.html')
    username=request.POST.get('username')
    password=request.POST.get('password')
    if user := authenticate(username=username, password=password):
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("L'utilisateur es desactive")
    else:
        return HttpResponse("Soit votre nom ou votre password est incorrect")  

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')




