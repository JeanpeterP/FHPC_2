from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import(
    #api_accounts,
    AccountListApiView,
    PetApiView,
    CustomTokenObtainPairView
)

urlpatterns=[
    #path("accounts/", api_accounts, name="api_salespersons")
    path('accounts/', AccountListApiView.as_view()),
    path('accounts/<int:pk>', AccountListApiView.as_view()),
    path('pets/', PetApiView.as_view()),
    path('pets/<int:pk>', PetApiView.as_view()),    
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenObtainPairView.as_view(),name='token_refresh'),
]