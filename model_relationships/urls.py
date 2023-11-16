"""
URL configuration for model_relationships project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from main import views

urlpatterns = [
    path('', views.show, name="home"),
    path('api/artists', views.save_or_fetch_artists, name="save_or_fetch_artists"),
    path('api/artists/<int:id>', views.fetch_one_artist, name="fetch_one_artists"),
    path('api/artists/<int:id>/delete', views.delete_artist, name="views.delete_artists"),
    path('api/artists/<int:id>/update', views.update_artist, name="views.update_artists"),
    path('api/artists/<int:id>/albums', views.albums_for_artist, name="views.albums_for_artists"),
    path('admin/', admin.site.urls),
]
# api/artists -> fetch artists ->GET
# api/artists -> create the  artists ->POST
# api/artists/18 -> details of 1 the  artists ->get
# api/artists/18/delete -> details of 1 the  artists ->DELETE
# api/artists/18/UPDATE -> details of 1 the  artists ->PUT/PATCH
