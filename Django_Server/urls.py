from django.contrib import admin
from django.urls import path
from CRUD_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employe-list/', views.employeList, name='employe_list')
]
