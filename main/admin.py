from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(DashboardIntro)
admin.site.register(Topic)
admin.site.register(Explanation)
admin.site.register(Disclaimer)