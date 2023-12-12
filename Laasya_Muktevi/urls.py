"""
URL configuration for Laasya_Muktevi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from wildcard import views

urlpatterns = [
    path('', views.wildcard_home, name='wildcard_home'),
    path('create/', views.create_contact_card, name='create_contact_card'),
    path('card_info/<int:card_id>/', views.card_info, name='card_info'),
]

