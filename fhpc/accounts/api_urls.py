from django.urls import path, include
from .api_views import(
    #api_accounts,
    AccountListApiView,
    PetApiView
)

urlpatterns=[
    #path("accounts/", api_accounts, name="api_salespersons")
    path('accounts/', AccountListApiView.as_view()),
    path('accounts/<int:pk>', AccountListApiView.as_view()),
    path('pets/', PetApiView.as_view()),
    path('pets/<int:pk>', PetApiView.as_view()),
]