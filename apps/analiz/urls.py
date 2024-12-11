from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_list, name='task_list'),
    path('add/', views.Library_add, name='task_add'),
    path('<int:pk>/edit/', views.library_edit, name='task_edit'),
    path('<int:pk>/delete/', views.library_delete, name='task_delete'),
]
