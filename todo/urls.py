from django.urls import path
from .views import TodoRudView, TodoCreateView, TodoListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('create/', TodoCreateView.as_view(), name='todo-create'),
    path('', TodoListView.as_view(), name='todo-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:pk>/', TodoRudView.as_view(), name='todo-rud'),
]
