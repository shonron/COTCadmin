from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from thechildrenofcorn.views import userfield, check, checkcredentials

urlpatterns = [
    path("", views.start, name= "start"),
    path('signup/', userfield),
     path('signin/', check)
    ]
    
urlpatterns += staticfiles_urlpatterns()