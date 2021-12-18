from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('segments-list/', views.apiSegmentList, name='segments-list'),
    path('segments-detail/<str:pk>/', views.apiSegmentDetail, name='segments-detail'),
    path('segments-create/', views.apiSegmentCreate, name='segments-create'),
    path('segments-update/<str:pk>/', views.apiSegmentUpdate, name='segments-update'),

    path('hello', views.hello, name='hello'),
]