"""WTS_3 URL Configuration

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
from DemoCar import views as DemoCar_views

urlpatterns = [
    path('',DemoCar_views.index,name='index'),
    path('movie.html', DemoCar_views.movie, name='movie'),
    path('racing.html', DemoCar_views.racing, name='racing'),
    path('show.html', DemoCar_views.show, name='show'),
    path('contact.html', DemoCar_views.contact, name='contact'),
    path('header.html',DemoCar_views.header, name='header'),
    path('footer.html',DemoCar_views.footer, name='footer'),
    path('index.html',DemoCar_views.index,name='index'),
    path('admin/', admin.site.urls),
]
