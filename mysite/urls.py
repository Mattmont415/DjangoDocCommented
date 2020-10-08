"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#include function allows rferencing other URLconfigurations
#chops off whatever part of the URL matched to that point
from django.urls import include, path

#Point to root URLconf at polls.urls
urlpatterns = [
    #Django starts at first pattern and moves its way down
    #wired the index view to URLconf
    path('polls/', include('polls.urls')),
    #The route is a string that contains a URL pattern
    #Pattern match? CALLS view with HTPR object as the first argument
    #captured values from the route as keyword arguments
    path('admin/', admin.site.urls),
]