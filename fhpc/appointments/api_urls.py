from django.urls import path, include
from .api_views import(
    AppointmentApiView
)

urlpatterns=[
    path('appointments/', AppointmentApiView.as_view()),
    path('appointments/<int:pk>', AppointmentApiView.as_view()),
]