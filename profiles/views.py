from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.conf import settings

from .models import DocchainUser
from django.contrib.auth.models import User


from profiles.forms import DocchainUserForm, DocchainUserInfoForm

# Create your views here.
def index(request):
    return HttpResponse("hello world")
    #return render(request, 'index.html')




def register(request):

    return render(request,'register.html')


def docchainRegister(request):
    registered = False
    if request.method == 'POST':
        user_form = DocchainUserForm(data=request.POST)
        profile_form = DocchainUserInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return HttpResponseRedirect('/')

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = DocchainUserForm()
        profile_form = DocchainUserInfoForm()

    return render(request,'register.html',
                        {'user_form':user_form,
                        'profile_form':profile_form,
                        'registered':registered})


def my_users(request):
    if request.method == 'POST':    
        username = request.POST.get('username')

        user = authenticate(username=username)

        if user:
            if user.is_authenticated:
                print('-------',user.username)
                u = User.objects.get(username = user.username)
                queryset = u.docchainuser.address
                print('**********', queryset)
                login(request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
                return HttpResponseRedirect('/dashboard')
            else:
                return HttpResponse('account not active')
        else:
            context = {
                'msg': 'Invalid username. Please try again.'
            }
            print('noott')
            return render(request,'login.html',context)

    else:
        return render(request, 'login.html')   



def special(request):
    return HttpResponse("you are logged in.")




def dashboard(request): 
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        current_user = request.user.username
        context = {
                'username': current_user,
            }
        return render(request,'index.html',context)
        
  
    

def new_account(request):
    #print(web3.geth.admin.node_info())
    return render(request, "create_account.html")


def PGDM_generate(request):
    return render(request, 'pgdm_generate.html')


def PGDMHR_generate(request):
    return render(request, 'pgdm_generate.html')

def PGDMNEW_generate(request):
    return render(request, 'pgdm_generate.html')