from django.urls import path
from .views import *

urlpatterns = [
    path('userreg',UserRegistration.as_view()),
    path('userreg/<int:id>/',UserRegistration.as_view())
]
