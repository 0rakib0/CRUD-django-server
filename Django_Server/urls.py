from django.contrib import admin
from django.urls import path
from CRUD_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employe-list/', views.employeList, name='employe_list'),
    path('employe/<int:id>/', views.singleEmploye, name='employe'),
    path('add-employe/', views.AddEmploye, name='add_employe'),
    path('update-employe/', views.updateEmploye, name='update_employe'),
    path('delete-employe/<int:id>/', views.deleteEmploye, name='delete_employe')
]
