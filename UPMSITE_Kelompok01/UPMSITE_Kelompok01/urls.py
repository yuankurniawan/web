"""UPMSITE_Kelompok01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from home import views as homeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeViews.homepage, name = "landingpage"),
    path('login/',homeViews.page_login, name = "login"),
    path('homepage/',homeViews.homepage, name = "homepage"),
    path('editform/',homeViews.dashboardForm, name="editform"),
    path('editfolderform/<id>',homeViews.informasiUmum_add_folder, name="editfolderform"),
    path('updateform/<str:file_id>/<str:folder_id>',homeViews.updateFile, name="updateform"),
    path('informasiUmum/',homeViews.informasiUmum, name="informasiUmum"),
    path('detail/<id>', homeViews.informasiUmumDetailView, name='detail'),
    path('detail1/<id>', homeViews.informasiUmumDetailView1, name='detail1'),
    path('akreditasiUmum/',homeViews.akreditasiUmum, name="akreditasiUmum"),
    path('auditprodi/',homeViews.auditProdi, name="auditprodi"),
    path('akreditasiprodi/',homeViews.akreditasiProdi, name="akreditasiprodi"),
    path('auditumum/',homeViews.auditUmum, name="auditumum"),
    path('logout/',homeViews.logout_user, name="logout"),
    path('<id>/delete', homeViews.delete_view, name="delete"),
    path('<id>/update', homeViews.update_view, name="update"),
    path('<id>/deletefolder', homeViews.delete_folder_view, name="deletefolder"),
    path('<id>/updatefolder', homeViews.update_folder_view, name="updatefolder"), 
]
