from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from cosmosreboot.forms import SignupForm
from django.contrib.auth.models import User
from .forms import InputForm
# from django.contrib.auth.decorators import login_required
# import requests

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def business(request):
    return render(request, 'pages/business.html')

def marketing(request):
    return render(request, 'pages/marketing.html')

def permitting(request):
    return render(request, 'pages/permitting.html')

def chat(request):
    return render(request, 'pages/chat.html')

def team(request):
    return render(request, 'pages/team.html')

def newbrunswick(request):
    return render(request, 'pages/newbrunswick.html')

def alberta(request):
    return render(request, 'pages/alberta.html')

def bc(request):
    return render(request, 'pages/bc.html')

def manitoba(request):
    return render(request, 'pages/manitoba.html')

def newfoundland(request):
    return render(request, 'pages/newfoundland.html')

def northwest(request):
    return render(request, 'pages/northwest.html')

def novascotia(request):
    return render(request, 'pages/novascotia.html')

def nunavut(request):
    return render(request, 'pages/nunavut.html')

def ontario(request):
    return render(request, 'pages/ontario.html')

def princeedward(request):
    return render(request, 'pages/princeedward.html')

def quebec(request):
    return render(request, 'pages/quebec.html')

def saskatchewan(request):
    return render(request, 'pages/saskatchewan.html')

def yukon(request):
    return render(request, 'pages/yukon.html')

def disclaimer(request):
    return render(request, 'pages/disclaimer.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def terms(request):
    return render(request, 'pages/terms.html')

@login_required
def dashboard(request):
    users = User.objects.all()
    return render(request, 'pages/dashboard.html',{'users': users})

@login_required
def profile(request):
    return render(request, 'pages/profile.html')

@login_required
def businesshub(request):
    return render(request, 'pages/businesshub.html')

@login_required
def marketinghub(request):
    return render(request, 'pages/marketinghub.html')

@login_required
def chat(request):
    return render(request, 'pages/chat.html')

@login_required
def businessplan(request):
    return render(request, 'pages/businessplan.html')

@login_required
def sopbuilder(request):
    return render(request, 'pages/sopbuilder.html')