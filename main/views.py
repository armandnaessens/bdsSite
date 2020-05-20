from django.shortcuts import render
from .models import*
from django.contrib.staticfiles.storage import staticfiles_storage
import json
import os
import pandas as pd
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
    with open('main/df_provincie.json', 'r') as myfile:
        data=myfile.read()
    provinciedata = json.loads(data)
    provincie_df =  pd.DataFrame.from_dict(provinciedata)

    return render(request, 'main/insights.html',
    {'excitementLabels':provincie_df['provincie'].to_list(),
    'excitementIndifferent':provincie_df['ratio average'].to_list(),
    'excitementOptimists':provincie_df['ratio super optimists'].to_list(),
    'excitementPessimists':provincie_df['ratio super pessimists'].to_list(),
    'hospitalizations100k':provincie_df['Hospitalizations per 100k inhabitants'].to_list(),
    'diffActivity':provincie_df['diff_activity'].to_list(),
    'diffRatio':provincie_df['diff_ratio'].to_list()
    })