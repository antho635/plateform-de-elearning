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
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return HttpResponseRedirect('login')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    content = {
        'registered': registered,
        'form1': user_form,
        'form2': profile_form,
    }
    return render(request, 'utilisateurs/register.html', content)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("L'utilisateur es desactive")
        else:
            return HttpResponse("Soit votre nom ou votre password est incorrect")
    else:
        return render(request, 'utilisateurs/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# curriculum view
def curriculum(request):
    return render(request, 'portfolio/curriculum.html')


# contactForm view
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redriect('/')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "form.html", {'form': form})


# Eco
def eco_demenagement(request):
    return render(request, 'portfolio/projet/projet_demenagement.html')


# Eco details
def eco_demenagement_details(request):
    return render(request, 'portfolio/projet/details/eco_demenagement_details.html')


# cv_index view
def cv_design(request):
    return render(request, 'portfolio/projet/details/cv-html_css.html')


# la_corddee_numerique view
def la_corddee_numerique(request):
    return render(request, 'portfolio/projet/la_cordee_numerique.html')


# pizzeria view
def pizzeria(request):
    return render(request, 'portfolio/projet/pizzeria.html')