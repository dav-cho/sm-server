from django.urls import path

from .views import UserListView, UserDetailView, GetUserDetailsView

urlpatterns = [
    path("", UserListView.as_view(), name="users"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("getuser/", GetUserDetailsView.as_view(), name="get-user"),
]
