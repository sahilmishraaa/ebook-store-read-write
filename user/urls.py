from django.urls import path
from .views import *

urlpatterns=[
    path('loginmanage/',loginmanage,name='loginmanage'),
    path('logoutmanage/',logoutmanage,name='logoutmanage'),
    path('loginpg/',loginpg,name='loginpg'),
    path('signup/',signup,name='signup'),
    path('account/', account, name='account'),
    path('logoutmanage/',logoutmanage,name='logoutmanage'),
    path('signupmanage/',signupmanage,name='signupmanage'),
    path('update_profile/', update_profile, name='update_profile'),
]