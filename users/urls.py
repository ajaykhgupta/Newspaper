from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SignUpView

urlpatterns = [
    path('signup/',SignUpView.as_view(),name = 'signup')

]