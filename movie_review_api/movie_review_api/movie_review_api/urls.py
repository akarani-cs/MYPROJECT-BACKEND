from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet
from users.views import UserViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponseRedirect


router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/api/')),  # redirect root to /api/
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # auth
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
