"""bdsSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
import pandas as pd
import numpy as np
import json

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('', include('main.urls')),
]

# df_rest = pd.read_csv("sentiment_rest.csv")
# df_test = pd.read_csv("sentiment_limburg.csv")
# df_hospitalizations = pd.read_csv("hospitalisations.csv")
# with open('inhabitants.json') as json_file:
#     inhabitants = json.load(json_file)
# df_test = df_test.append(df_rest)
# df_test = df_test.drop(columns=['Unnamed: 0'])
# df_test.Datetime = pd.to_datetime(df_test['Datetime'])
# df_test['day'] = df_test['Datetime'].dt.date
# df_test_sentiment = df_test[df_test['sentiment'].notnull() & (df_test['lang'] == 'nl')]
# df_test_sentiment['sentiment'] = np.where(df_test_sentiment['sentiment']>=0.5, 1, 0)
# df_test_sentiment
# df_test['day'] = df_test['Datetime'].dt.date
# df_tweets_per_day = df_test.groupby(['screen_name','day']).size().to_frame(name = 'tweetsPerDay').reset_index()
