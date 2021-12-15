from django.urls import path
from .views import CookieDetail, CookieList

urlpatterns = [
    path("", CookieList.as_view(), name="cookie_stands_list"),
    path("<int:pk>/", CookieDetail.as_view(), name="cookie_stands_detail"),
]
