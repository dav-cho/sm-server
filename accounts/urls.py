from django.urls import path

from .views import UserListView, UserDetailView, CurrentUserView

urlpatterns = [
    path("", UserListView.as_view(), name="users"),
    path("user/", CurrentUserView.as_view(), name="current-user"),
    path("<username>/", UserDetailView.as_view(), name="user-detail"),
    # path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
