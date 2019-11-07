from django.urls import path
from . import views

app_name = 'quizbop_app' # for namespacing
urlpatterns = [
    path('', views.hello, name='hello world')
]