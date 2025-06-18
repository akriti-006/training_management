from django.urls import path

from .views.cb_views import(
    PlListView, PlAddView, PlDetailView, PlUpdateView, PlDeleteView,
    FwAddView, FwListView, FwDetailView, FwUpdateView, FwDeleteView,

    CdAddView, CdListView, CdDetailView, CdUpdateView, CdDeleteView,
    TeAddView, TeListView, TeDetailView, TeUpdateView, TeDeleteView, TeStartView,
    SeListView, SeDetailView, SeUpdateView,
)

# from .views.generic_views_custom import (
#     PlListView, PlAddView, PlDetailView,
#     PlUpdateView, PlDeleteView,
#     FwListView, FwAddView, FwDetailView, FwUpdateView,FwDeleteView
#     )


app_name = 'shared-app'

urlpatterns = [
    
    path('programming-language/list/', PlListView.as_view(), name='programming-language-list'),
    path('programming-language/add/', PlAddView.as_view(), name='programming-language-add'),
    path('programming-language/<int:pk>/detail/', PlDetailView.as_view(), name='programming-language-detail'),
    path('programming-language/<int:pk>/update/', PlUpdateView.as_view(), name='programming-language-update'),
    path('programming-language/<int:pk>/delete/', PlDeleteView.as_view(), name='programming-language-delete'),

    path('framework/list', FwListView.as_view(), name='framework-list'),
    path('framework/add/', FwAddView.as_view(), name='framework-add'),
    path('framework/<int:pk>/detail/', FwDetailView.as_view(), name='framework-detail'),
    path('framework/<int:pk>/update/', FwUpdateView.as_view(), name='framework-update'),
    path('framework/<int:pk>/delete/', FwDeleteView.as_view(), name='framework-delete'),

    path('course-data/list/', CdListView.as_view(), name='course-data-list'),
    path('course-data/add/', CdAddView.as_view(), name='course-data-add'),
    path('course-data/<int:pk>/detail/', CdDetailView.as_view(), name='course-data-detail'),
    path('course-data/<int:pk>/update/', CdUpdateView.as_view(), name='course-data-update'),
    path('course-data/<int:pk>/delete/', CdDeleteView.as_view(), name='course-data-delete'),

    path('training-enquiry/list/', TeListView.as_view(), name='training-enquiry-list'),
    path('training-enquiry/add/', TeAddView.as_view(), name='training-enquiry-add'),   
    path('training-enquiry/<int:pk>/detail/', TeDetailView.as_view(), name='training-enquiry-detail'),
    path('training-enquiry/<int:pk>/update/', TeUpdateView.as_view(), name='training-enquiry-update'),
    path('training-enquiry/<int:pk>/delete/', TeDeleteView.as_view(), name='training-enquiry-delete'),
    
    path('training-enquiry/<int:pk>/start/', TeStartView.as_view(), name='training-enquiry-start'),

    path('student-enrollment/list/', SeListView.as_view(), name='course-enrollment-list'),
    path('student-enrollment/<int:pk>/detail/', SeDetailView.as_view(), name='course-enrollment-detail'),
    path('student-enrollment/<int:pk>/update/', SeUpdateView.as_view(), name='course-enrollment-update'),

]
