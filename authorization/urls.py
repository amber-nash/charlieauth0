"""authorization URL Configuration

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
from django.conf.urls import include
from auth0login import views
import http.client

# conn = http.client.HTTPSConnection("")

# headers = { 'authorization': "Bearer YOUR_MGMT_API_ACCESS_TOKEN" }

# conn.request("GET", "/dev-aykh4rgv.us.auth0.com/api/v2/users/USER_ID", headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
    path('api/v2/users/{id}', views.v2search)
]

