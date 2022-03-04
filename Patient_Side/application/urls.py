"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from Patient import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('medicalneed/', views.medical_need, name='medicalneed'),
    path('nonmedicalneed/', views.non_medical_need, name='nonmedicalneed'),
    path('roomnumber/', views.get_room_number, name='roomnumber'),
    path('requestsent/', views.request_sent, name='requestsent'),
    path('nonurgentquestion/', views.non_urgent_question, name='nonurgentquestion'),
    path('admin/', admin.site.urls),
]
