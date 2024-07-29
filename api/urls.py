from django.urls import path, include
from Authentication.views import RegisterView, LoginView, PersonView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('person/', PersonView.as_view()),
]