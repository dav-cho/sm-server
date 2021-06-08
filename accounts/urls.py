from django.urls import path

from .views import UserList, UserDetail, RegisterUser

urlpatterns = [
    path("", UserList.as_view(), name="users"),
    path("<int:pk>/", UserDetail.as_view(), name="user-detail"),
    path("register/", RegisterUser.as_view(), name="register"),
]
