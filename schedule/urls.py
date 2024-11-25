from django.urls import path
from .views import ScheduleList, ScheduleCreate, ScheduleUpdate, ScheduleDelete, home_view, contact_view,  schedule_complete

app_name = 'schedule'

urlpatterns = [
    path('', home_view, name='home'),
    path('schedules/', ScheduleList.as_view(), name='schedule_list'),
    path('create/', ScheduleCreate.as_view(), name='schedule_create'),
    path('update/<int:pk>/', ScheduleUpdate.as_view(), name='schedule_update'),
    path('delete/<int:pk>/', ScheduleDelete.as_view(), name='schedule_delete'),
    path('contact/', contact_view, name='contact'),
    path('schedule/<int:pk>/complete/', schedule_complete, name='complete_schedule'), 
]