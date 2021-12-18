from django.urls import path

from .views import home, signup, addPassword, getPasswords, filter

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('addPassword/', addPassword, name="addPassword"),
    path('passwords/<int:id>/', getPasswords, name="passwords"),
    path('passwords/<int:id>/filter/', filter, name="filter")
]