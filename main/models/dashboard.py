from django.db import models

class DashboardIntro(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    active = models.BooleanField(default = False)

    def save(self, *args,**kwargs):
        if self.active:
            try:
                temp = DashboardIntro.objects.get(active = True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except DashboardIntro.DoesNotExist:
                pass
        super(DashboardIntro,self).save(*args, **kwargs)
    def __str__(self):
        return "Dashboard Intro - " + self.name 

class Topic(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    active = models.BooleanField(default = False)

    def save(self, *args,**kwargs):
        if self.active:
            try:
                temp = Topic.objects.get(active = True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except Topic.DoesNotExist:
                pass
        super(Topic,self).save(*args, **kwargs)
    def __str__(self):
        return " " + self.name 