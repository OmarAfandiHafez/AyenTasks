from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.TasksListCreateAPIView.as_view()),
    path('task/<int:pk>/', views.TaskRetrieveUpdateAPIView.as_view()),
    path('change-task-state/<int:pk>/', views.ChangeTaskState.as_view()),
    path('link-tasks/<int:first_task_pk>/<int:second_task_pk>/', views.LinkTasksAPIView.as_view()),
    path('unlink-tasks/<int:pk>/', views.UnlinkTasksAPIView.as_view()),
]
