from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')

def insights(request):
    return render(request, 'main/insights.html')