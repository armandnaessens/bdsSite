from django.shortcuts import render
from .models import*

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def dashboard(request):
    try:
        intro = DashboardIntro.objects.get(active = True)
    except:
        intro = ''
    topics = Topic.objects.all()
    return render(request, 'main/dashboard.html', {'intro':intro, 'topics':topics})

def insights(request):
    return render(request, 'main/insights.html')