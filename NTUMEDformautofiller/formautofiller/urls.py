from django.urls import path
from . import views


urlpatterns = [

]

urlpatterns += [   
    path('input/', views.user_input, name='user-input'),
]