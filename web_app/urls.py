from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("services/", services, name="services"),
    path("study/", study, name="study"),
    path("contact/", contact, name="contact"),
    path("case1/", case1 , name="case1"),
    path("case2/", case2 , name="case2"),
    path("case3/", case3 , name="case3"),
    path("case4/", case4 , name="case4"),
    path("case5/", case5 , name="case5"),
    path("case6/", case6 , name="case6"),
]

urlpatterns += staticfiles_urlpatterns()