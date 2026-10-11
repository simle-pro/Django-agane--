from django.urls import path
from .views import *

urlpatterns = [
    path('groups/', group_list, name='group_list'),
    path('groups/<int:pk>/', group_detail, name='group_detail'), # Детали группы
    path('groups/add/', group_create, name='group_create'),
    path('groups/edit/<int:pk>/', group_update, name='group_update'),
    path('groups/delete/<int:pk>/', group_delete, name='group_delete'),
    path('', student_list, name='student_list'),
    path('students/<int:pk>/', student_detail, name='student_detail'), 
    path('students/add/', student_create, name='student_create'),
    path('students/edit/<int:pk>/', student_update, name='student_update'),
    path('students/delete/<int:pk>/', student_delete, name='student_delete'),
]