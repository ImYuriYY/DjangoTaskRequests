from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^user/(?P<userLogin>\D+)/(?P<nameFolder>\D+)/(?P<idFolder>\d+)/', user, name="user"),
    path('user/<str:userLogin>/<str:nameFolder>/', user, name="user"),
    path('user/<str:userLogin>/', user, name="user"),
    path('user/', user, name="user"),
    path('', index, name="home"),
    path('error/', error, name="error"),

]