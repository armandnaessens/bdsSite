from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
from .models import *

admin.site.register(DashboardIntro)
@admin.register(Topic)
class TopicAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
@admin.register(Explanation)
class ExplanationAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(Disclaimer)
class DisclaimerAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
