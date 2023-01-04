from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   path('index/',views.index.as_view(),name='index'),
   path('view_employee/',views.view_employee.as_view(),name='view_employee'),
   path('add_employee/',views.add_employee.as_view(),name='add_employee'),
   path('remove_employee/',views.remove_employee.as_view(),name='remove_employee'),
   path('remove_employee/<int:emp_id>',views.remove_employee.as_view(),name='remove_employee'),
   path('filter_employee/',views.filter_employee.as_view(),name='filter_employee'),

]
