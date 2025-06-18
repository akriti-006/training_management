from django.urls import path

from .views import (
    HomeStuView, ListStuView, AddStuView,
    DetailStuView, UpdateStuView, DeleteStuView,
    
)

urlpatterns = [
    path('stu/home/', HomeStuView.as_view(), name='stu-home'),
    path('stu/list/', ListStuView.as_view(), name='stu-list'),
    path('stu/add/', AddStuView.as_view(), name='stu-add'),
    path('stu/<int:pk>/detail/', DetailStuView.as_view(), name='stu-detail'),
    path('stu/<int:pk>/update/', UpdateStuView.as_view(), name='stu-update'),
    path('stu/<int:pk>/delete/', DeleteStuView.as_view(), name='stu-delete'),
]
