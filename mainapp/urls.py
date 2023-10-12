from mainapp.views import UserView
from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)


router = DefaultRouter()
router.register('user', UserView)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]

urlpatterns += router.urls