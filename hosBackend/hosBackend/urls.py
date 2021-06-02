"""hosBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hosDjango import views as hosloc_Views

router = DefaultRouter()
router.register('hosloc',hosloc_Views.LocInfoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('<str:city>/city/',hosloc_Views.cityHos),
    # path('cityHosDis/',hosloc_Views.cityHosDis),
    path('<str:county>/county/',hosloc_Views.CounryHos),
    path('<str:city>/city/<str:county>/county/',hosloc_Views.cityCountryHos),
    path('<str:city>/city/<str:county>/county/<str:subject>/subject/', hosloc_Views.AllHos),
    # path('/<str:city>/det/',hosloc_Views.selectCity, name ='cityDet'),
]
