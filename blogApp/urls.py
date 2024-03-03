from django.urls import path
from.views import *
urlpatterns = [
    path("",index,name="index"),
    path("register/",register,name="register"),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
    path("newpost/",newPost,name="newpost"),
    path("postdetails/<int:id>",postDetail,name="postdetail")
]
