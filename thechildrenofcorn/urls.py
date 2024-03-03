from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from thechildrenofcorn.views import userfield

urlpatterns = [
    path("", views.start, name= "start"),
    path('create/', userfield)
    ]
    
urlpatterns += staticfiles_urlpatterns()