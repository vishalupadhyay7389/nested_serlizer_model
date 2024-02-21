from django.urls import path
from .views import InsulatorListView , CourseListView

urlpatterns = [
    path('instructor/', InsulatorListView.as_view() , name='instructor'),
    path('course/', CourseListView.as_view() , name='course'),
]