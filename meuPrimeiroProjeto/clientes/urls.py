from django.urls import path, include
from .views import persons_list
from .views import persons_new

urlpatterns = [
    path('list/', persons_list, name="persons_list"),
    path('new/', persons_new, name="persons_new"),
]
