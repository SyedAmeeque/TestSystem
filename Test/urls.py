"""
URL configuration for System project.

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
from django.urls import path, include
from .Views.Signup import Signup
from .Views.login import Login
from .Views.logout import Logout
from .Views.base import Base
from .Views.index import Home
from .Views.thanks import Thank



urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('Instructions/', Base.as_view(), name='Instructions'),
    path('Exam/', Home.as_view(), name='Exam'),
    path('exam/completed/successfully/page/Thanks/', Thank.as_view(), name='thanks'),
]




