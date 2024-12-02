"""
URL configuration for rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sample_fun),
    path('model',views.model_view),
    path('update/<id>',views.update_view),
    path('fun',views.fun1),
    path('fun2/<id>',views.fun2),
    path('class1',views.fun7.as_view()),
    path('class2/<d>',views.fun8.as_view()),
    path('add',views.add.as_view()),
    path('update1/<id>',views.update.as_view()),

]
