from django.urls import path
from . import views

urlpatterns = [
    path('meta-data/', views.MetaDataListCreateAPIView.as_view()),
    path('meta-data/<int:pk>/', views.MetaDataRetrieveAPIView.as_view()),
    path('document/', views.DocumentListCreateAPIView.as_view()),
    path('document/<int:pk>/', views.DocumentRetrieveAPIView.as_view()),
]
