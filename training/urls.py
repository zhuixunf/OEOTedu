from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('courses_list/', views.courses_list, name='courses_list'),
    path('course_edit/<int:id>/', views.course_edit, name='course_edit'),
    path('post_add/', views.post_add, name='post_add'),
    path('post/detail/<int:id>/', views.post_detail, name='post_detail'),
    path('post/update/<int:id>/', views.post_update, name='post_update'),
    path('post_delete/<int:id>/', views.post_delete, name='post_delete'),
    path('company/', views.company, name='company'),
]
